import utility as util
import collision as col
import scene_manager as SM
import game_obj
import pygame

x_center = util.screen.get_width() / 2
y_center = util.screen.get_height() / 2
width = 600
height = 600
pos = [x_center - (width / 2), y_center - (height / 2)]

class inside_pc(game_obj.game_object):
    def setup(self):
        print("self.sprite")
        self.sprite_path = "art/mao.png"
        self.sprite = pygame.image.load(self.sprite_path)
        self.sprite = pygame.transform.scale(self.sprite, (width, height))

    def draw(self):
        util.screen.blit(self.sprite, (self.pos_x, self.pos_y))
        

workplace = inside_pc(SM.SCENES.PC, pos[0], pos[1], None)

class return_arrow(game_obj.game_object):
    def setup(self):
        self.pos_x = 60
        self.pos_y = 60

        self.collider_list = col.collider(0, (self.pos_x, self.pos_y), (50, 20))


    def update(self):
        if (self.is_colliding and util.mouse_pressed):
            SM.current_scene = SM.SCENES.DESK.value

return_arrow_obj = return_arrow(SM.SCENES.PC)