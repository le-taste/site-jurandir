import pygame
from enum import Enum

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
mouse_pressed = False
dt = 0

def global_from_relative(relative_pos_x, relative_pos_y, parent_pos_x, parent_pos_y):
    return [parent_pos_x + relative_pos_x, parent_pos_y + relative_pos_y]

class COMPONENTS(Enum):
    RAM = 0
    CPU = 1
    PLACAMAE = 2
    PSU = 3
    GPU = 4
    HDD = 5