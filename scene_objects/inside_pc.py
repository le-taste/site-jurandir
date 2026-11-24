import utility as util
import collision as col
from game_loop import problem_manager as PM
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
        self.sprite = art.pc_inside
        self.sprite = art.scale_image(self.sprite, width, height)

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

surface = pygame.Surface((util.screen_width, util.screen_height), pygame.SRCALPHA)

class pc_component(game_obj.game_object):
    def __init__(self, component, *args):
        self.component = component
        self.mouse_pstate = False
        self.debug = False
        super().__init__(*args)
        self.collider_list = list()

    def add_colliders(self, *args):
        for collider in args:
            self.collider_list.append(collider)


    def update(self):
        if (self.is_colliding and util.mouse_pressed and (self.mouse_pstate != util.mouse_pressed)):
            PM.problem_manager_obj.tried_solution(self.component)

        self.mouse_pstate = util.mouse_pressed
    
    def draw(self):
        if (self.collider_list == None or not self.debug): return

        for collider in self.collider_list:
            if (collider.type == 0):
                pygame.draw.rect(util.screen, self.color, (collider.pos[0], collider.pos[1], collider.shape[0], collider.shape[1]))

CPU = pc_component(util.COMPONENTS.CPU, SM.SCENES.PC)
cpu_pos = util.global_from_relative(130, 190, workplace.pos_x, workplace.pos_y)
CPU.add_colliders(col.collider(0, cpu_pos, (120, 120)))

RAM = pc_component(util.COMPONENTS.RAM, SM.SCENES.PC)
ram_pos = util.global_from_relative(270, 190, workplace.pos_x, workplace.pos_y)
RAM.add_colliders(col.collider(0, ram_pos, (60, 160)))

PSU = pc_component(util.COMPONENTS.PSU, SM.SCENES.PC)
psu_pos = (workplace.pos_x + 10, workplace.pos_y + 30)
PSU.add_colliders(col.collider(0, psu_pos, (210, 100)))

GPU = pc_component(util.COMPONENTS.GPU, SM.SCENES.PC)
gpu_pos = util.global_from_relative(70, 435, workplace.pos_x, workplace.pos_y)
shape = (320, 40)
GPU.add_colliders(col.collider(0, gpu_pos, shape), col.collider(0,(gpu_pos[0], gpu_pos[1] + 80), shape))
GPU.debug = True

return_arrow_obj = return_arrow(SM.SCENES.PC)