import pygame

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
mouse_pressed = False
dt = 0

def global_from_relative(relative_pos_x, relative_pos_y, parent_pos_x, parent_pos_y):
    return [parent_pos_x + relative_pos_x, parent_pos_y + relative_pos_y]