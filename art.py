import pygame

def process_image(sprite_path):
    return pygame.image.load(sprite_path)

def scale_image(sprite, new_width, new_height):
    return pygame.transform.scale(sprite, (new_width, new_height))

def scale_image_by_magnitude(sprite, new_scale):
    return pygame.transform.scale_by(sprite, new_scale)


start_screen_background = process_image("art/start_screen_background.png")
lula_image = process_image("art/lula.png")
mao_image = process_image("art/mao.png")
start_button_image = process_image("art/start_button.png")
jurandir_intro = process_image("art/jurandir_intro.png")
arrow = process_image("art/arrow.png")
day = process_image("art/day.png")
night = process_image("art/night.png")
jurandir = process_image("art/jurandir.png")
table = process_image("art/table.png")
pc = process_image("art/pc.png")