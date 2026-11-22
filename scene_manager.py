from enum import Enum

current_scene = 1
scene_list = list()

class scene:
    def __init__(self):
        scene_list
        self.scene_index = current_scene + 1
        self.game_obj_list = list()

        scene_list.append(self)

class SCENES(Enum):
    GAMESTART = 0
    DESK = 1
    PC = 2

game_start_scene = scene()
desk_scene = scene()
pc_scene = scene()