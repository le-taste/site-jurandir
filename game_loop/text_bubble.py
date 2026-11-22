import game_obj
import pygame
import scene_manager as SM
import utility as util
import math

class text_bubble(game_obj.game_object):

    def __init__(self, message, *args):
        super().__init__(*args)

        self.text = None
        self.text_index = 0
        self.counter = 0
        self.font = None
        self.message = message
        self.message_len = len(message)

        self.intensity = 5
        self.frequency = 2
        self.size = 32
        self.counter = 0

    def change_size(self, new_size):
        self.size = new_size

        self.font = pygame.font.Font("game_loop/pixel-sans-mono.ttf", self.size)
        self.text = self.font.render(self.message, True, (255, 255, 255))
        print(self.text.get_width())



    def setup(self):
        self.font = pygame.font.Font("game_loop/pixel-sans-mono.ttf", self.size)
        self.text = self.font.render(self.message, True, (255, 255, 255))

        self.counter = 0
        self.text_index = 0

    def update(self):
        self.counter += util.dt
        self.pos_y += (math.sin(self.counter * self.frequency) * self.intensity)

    def draw(self):
        util.screen.blit(self.text, (self.pos_x, self.pos_y))
