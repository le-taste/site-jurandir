import utility as util
import collision as col
import scene_manager as SM
import game_obj
import art
import math
import pygame

x_center = util.screen.get_width() / 2
y_center = util.screen.get_height() / 2
width = 600
height = 600
pos = [x_center - (width / 2), y_center - (height / 2)]

class inside_pc(game_obj.game_object):
    def setup(self):
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

        self.counter = 0

        self.flipped_image = pygame.transform.flip(art.arrow, True, False)
        self.sprite = art.scale_image_by_magnitude(self.flipped_image, 4)
        width = self.sprite.get_width()
        height = self.sprite.get_height()

        self.collider_list = col.collider(0, (self.pos_x, self.pos_y), (width, height))

    def just_collided(self):
        self.sprite = art.scale_image_by_magnitude(self.flipped_image, 4.2)

    def stopped_colliding(self):
        self.sprite = art.scale_image_by_magnitude(self.flipped_image, 4)

    def update(self):
        if (self.is_colliding and util.mouse_pressed):
            SM.current_scene = SM.SCENES.DESK.value

        self.counter += util.dt
        self.pos_y +=  math.sin(self.counter * 2) * 0.06

return_arrow_obj = return_arrow(SM.SCENES.PC)