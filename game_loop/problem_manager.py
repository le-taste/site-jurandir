import game_obj
import random
from enum import Enum
from . import problem_text
import utility as util
import scene_manager as SM

QUESTS = list()

QUESTS= [ 
    [(util.COMPONENTS.RAM, "Memória RAM danificada"), [ (util.COMPONENTS.CPU, "Very bad sir") ], (util.COMPONENTS.RAM, "Trocar resolveu  problema")],
    [(util.COMPONENTS.CPU, "CPU TA UMA BOSTA"), [ (util.COMPONENTS.CPU, "Very bad sir") ], (util.COMPONENTS.CPU, "Trocar resolveu problema")]
]

USABLE_QUESTS = QUESTS

class problem_manager(game_obj.game_object):

    def __init__(self, *args):
        quest_index = random.randrange(len(USABLE_QUESTS))
        self.question = USABLE_QUESTS[quest_index]
        USABLE_QUESTS.remove(self.question)

        self.problem_text_obj = problem_text.text_prefab(str(self.question[0][1]), SM.SCENES.DESK)

        self.should_update_problem = False

        self.counter = 0

        super().__init__(*args)

    def tried_solution(self, component):

        if (component == self.question[2][0]):
            SM.current_scene = SM.SCENES.DESK.value

            game_obj.destroy(self.problem_text_obj)

            self.problem_text_obj = problem_text.text_prefab(self.question[2][1], SM.SCENES.DESK)

            self.should_update_problem = True
        else:
            for message_component_pair in self.question[1]:
                if (component == message_component_pair[0]):
                    print(message_component_pair[1])

    def update(self):
        if (self.should_update_problem):
            self.counter += util.dt

            if (self.counter >= 3):

                game_obj.destroy(self.problem_text_obj)

                quest_index = random.randrange(len(USABLE_QUESTS))
                self.question = USABLE_QUESTS[quest_index]
                USABLE_QUESTS.remove(self.question)

                self.problem_text_obj = problem_text.text_prefab(str(self.question[0][1]), SM.SCENES.DESK)
                self.problem_text_obj.setup()
                self.counter = 0
                self.should_update_problem = False


problem_manager_obj = problem_manager(SM.SCENES.DESK)
SM.pc_scene.game_obj_list.append(problem_manager_obj)