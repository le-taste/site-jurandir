import game_obj
import random
from enum import Enum
from . import problem_text
import scene_manager as SM

class COMPONENTS(Enum):
    RAM = 0
    CPU = 1
    PLACAMAE = 2

QUESTS = list()

QUESTS= [ 
    [(COMPONENTS.RAM, "Memória RAM danificada"), ( (COMPONENTS.CPU, "Very bad sir") ), (COMPONENTS.RAM, "Trocar resolveu  problema")],
    [(COMPONENTS.RAM, "Memória RAM danificada"), ( (COMPONENTS.CPU, "Very bad sir") ), (COMPONENTS.RAM, "Trocar resolveu problema")]
]

USABLE_QUESTS = QUESTS

problem_is_displayed = False

class problem_manager(game_obj.game_object):

    def setup(self):
        global problem_is_displayed

        if (not problem_is_displayed):
            quest_index = random.randrange(len(USABLE_QUESTS))
            question = USABLE_QUESTS[quest_index][0]

            problem_text.text_prefab(str(question[1]), SM.SCENES.DESK)

            problem_is_displayed = True

    def update(self):
        global problem_is_displayed

        if (not problem_is_displayed):
            question = random.choice(USABLE_QUESTS)

            problem_text.text_prefab(question[1], SM.SCENES.DESK)

            problem_is_displayed = True

problem_manager(SM.SCENES.DESK)