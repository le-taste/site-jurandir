import game_obj
import art
import scene_manager as SM
import utility as util
import collision as col
import math
from game_loop import text_bubble

screen_width = util.screen.get_width()
screen_height = util.screen.get_height()

class start_screen(game_obj.game_object):
    def __init__(self, *args):
        self.counter = 0
        self.continue_button = None
        self.jurandir = None
        self.jurandir_start_pos = (190, 540)
        self.jurandir_end_pos = (910, 540)
        self.jurandir_speed = 5

        self.images = [
            art.scale_image(art.start_screen_background, screen_width, screen_height),
            art.scale_image(art.jurandir_intro, screen_width, screen_height),
            art.scale_image(art.night, screen_width, screen_height),
            art.scale_image(art.day, screen_width, screen_height)
        ]

        self.current_image = self.images[0]
        self.image_counter = 0

        #   evitar clique duplo do mouse
        self.past_mouse_pressed = False

        super().__init__(*args)

    def change_image(self):
        if (self.image_counter + 1 >= len(self.images)):
            SM.current_scene = SM.desk_scene
        else:
            self.image_counter += 1      
            
        self.current_image = self.images[self.image_counter]

        if self.image_counter == 1:
            self.continue_button = game_obj.game_object(SM.SCENES.GAMESTART)
            self.continue_button.sprite = art.scale_image_by_magnitude(art.arrow, 4)

            button_width = self.continue_button.sprite.get_width()
            button_height = self.continue_button.sprite.get_height()

            button_pos = (screen_width - button_width - 20, 15)
            self.continue_button.pos_x = button_pos[0]
            self.continue_button.pos_y = button_pos[1]

            self.continue_button.collider_list = col.collider(0, (button_pos[0], button_pos[1] - 1), (button_width, button_height + 2))

    def update(self):

        if self.image_counter == 3 and self.jurandir == None:
            self.counter += util.dt

            if (self.counter >= 1):
                self.jurandir = game_obj.game_object(SM.SCENES.GAMESTART)
                self.jurandir.sprite = art.scale_image_by_magnitude(art.jurandir, 0.2)
                self.jurandir.pos_x = self.jurandir_start_pos[0]
                self.jurandir.pos_y = self.jurandir_start_pos[1]

                self.counter = 0

        elif self.image_counter == 3:
            self.counter += util.dt

            if (self.jurandir.pos_x < self.jurandir_end_pos[0]):
                self.jurandir.pos_x += self.counter * self.jurandir_speed
            else:
                SM.current_scene += 1
            

        if self.image_counter == 2:
            self.counter += util.dt

            if (self.counter >= 2):
                self.change_image()
                self.counter = 0

        if (self.continue_button == None): return
        self.counter += util.dt
        self.continue_button.pos_y += (math.sin(self.counter * 2) * 0.06)

        if (self.continue_button.is_colliding):
            self.continue_button.sprite = art.scale_image_by_magnitude(art.arrow, 4.2)
        else:
            self.continue_button.sprite = art.scale_image_by_magnitude(art.arrow, 4)

        if (self.continue_button.is_colliding and util.mouse_pressed):
            self.change_image()
            game_obj.destroy(self.continue_button)
            self.continue_button = None

            self.counter = 0
            

    def draw(self):
        util.screen.blit(self.current_image, (0, 0))



class start_button(game_obj.game_object):

    def __init__(self, start_screen_obj:start_screen, *args):
        super().__init__(*args)
        self.button_image = art.scale_image_by_magnitude(art.start_button_image, 5)

        self.recalculate_pos()

        self.start_screen_obj = start_screen_obj
        self.collider_list = col.collider(0, (self.pos_x, self.pos_y), (self.width, self.height))

        self.counter = 0
        self.text_obj = None

    def recalculate_pos(self):
        self.width = self.button_image.get_width()
        self.height = self.button_image.get_height()

        self.pos_x = (util.screen.get_width()- self.width) / 2
        self.pos_y = (util.screen.get_height() - self.height) / 2 + 100

    def recalculate_text_pos(self):
        text_width = self.text_obj.text.get_width()
        text_height = self.text_obj.text.get_height()

        text_pos_rel = ((self.width - text_width) / 2, (self.height - (text_height - 25)) / 2)
        text_pos_global = util.global_from_relative(text_pos_rel[0], text_pos_rel[1], self.pos_x, self.pos_y)

        self.text_obj.pos_x = text_pos_global[0]
        self.text_obj.pos_y = text_pos_global[1]

    def setup(self):
        self.text_obj = text_bubble.text_bubble("START", SM.SCENES.GAMESTART)
        self.text_obj.intensity = 0.1
        self.text_obj.size = 76

        self.text_obj.setup()
        self.recalculate_text_pos()

    def just_collided(self):
        self.button_image = art.scale_image_by_magnitude(art.start_button_image, 5.5)
        self.recalculate_pos()

        self.text_obj.change_size(81)
        self.recalculate_text_pos()

    def stopped_colliding(self):
        self.button_image = art.scale_image_by_magnitude(art.start_button_image, 5)
        self.recalculate_pos()

        self.text_obj.change_size(76)
        self.recalculate_text_pos()

    def update(self):
        if (self.is_colliding and util.mouse_pressed):
            self.start_screen_obj.change_image()
            game_obj.destroy(self.text_obj)
            game_obj.destroy(self)

        self.counter += util.dt
        self.pos_y += (math.sin(self.counter * 2) * 0.1)


    def draw(self):
        util.screen.blit(self.button_image, (self.pos_x, self.pos_y))

start_screen_obj = start_screen(SM.SCENES.GAMESTART)
start_button(start_screen_obj, SM.SCENES.GAMESTART)