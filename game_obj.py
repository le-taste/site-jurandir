import utility as util
import scene_manager as SM

class game_object:
    def __init__(self, *args):
        self.pos_x = 0
        self.pos_y = 0
        self.collider_list = None

        self.scene = args[0].value
        SM.scene_list[self.scene].game_obj_list.append(self)

        self.color = "white"
        self.is_colliding = False

        self.sprite_path = ""
        self.sprite = None

        size = len(args)
        

        if (size >= 3):
            self.pos_x = args[1]
            self.pos_y = args[2]
        if (size >= 4):
            self.collider_list = args[3]
        elif (size >= 5):
            self.sprite_path = args[4]


    def just_collided(self):
        pass

    def stopped_colliding(self):
        pass

    def setup(self):
        pass

    def update(self):
        pass

    def draw(self):
        if (self.sprite == None):
            return
        util.screen.blit(self.sprite, (self.pos_x, self.pos_y))


def destroy(obj:game_object):
    SM.scene_list[obj.scene].game_obj_list.remove(obj)