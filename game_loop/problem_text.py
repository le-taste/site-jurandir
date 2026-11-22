import pygame
import game_obj
import utility as util
import scene_manager as SM

class text_prefab(game_obj.game_object):

    def __init__(self, message, *args):
        self.text = None
        self.text_index = 0
        self.counter = 0
        self.font = None
        self.message = message
        self.message_len = len(message)

        super().__init__(*args)

    def setup(self):
        self.font = pygame.font.Font("game_loop/pixel-sans-mono.ttf", 32)
        self.text = self.font.render("", True, (255, 255, 255))

        self.counter = 0
        self.text_index = 0

    def update(self):
        if not (self.text_index < self.message_len):
            return

        if (self.counter >= 0.01):
            next = self.text_index + 1
            if (next < self.message_len):
                if (self.message[next] == ' '):
                    self.text_index += 1

            self.text = self.font.render(self.message[0:self.text_index], True, (255, 255, 255))
            
            self.text_index += 1
            self.counter = 0
        else:
            self.counter += util.dt

    def draw(self):
        util.screen.blit(self.text, (40, 40))