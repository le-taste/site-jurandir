import pygame
import collision as col
import game_obj
import utility as util
import scene_manager as SM
from scene_objects import desk, inside_pc, game_start
from game_loop import problem_text
from game_loop import text_bubble

# pygame setup
pygame.init()

clock = pygame.time.Clock()
running = True

scene = SM.current_scene

for obj in SM.scene_list[SM.current_scene].game_obj_list:
    obj.setup()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            util.mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            util.mouse_pressed = False

    util.screen.fill("black")

    if (scene != SM.current_scene):
        for obj in SM.scene_list[SM.current_scene].game_obj_list:
            obj.setup()
        scene = SM.current_scene

    mouse_pos = pygame.mouse.get_pos()

    for obj in SM.scene_list[SM.current_scene].game_obj_list:

        obj.update()

        try: 
            for collider in obj.collider_list:
                if (collider.collides_with_point(mouse_pos)):
                    if (not obj.is_colliding):
                        obj.just_collided()
                        obj.is_colliding = True

                elif (obj.is_colliding):
                    obj.stopped_colliding()
                    obj.is_colliding = False
        except:

            try:
                collider = obj.collider_list

            
                if (collider.collides_with_point(mouse_pos)):
                    if (not obj.is_colliding):
                        obj.just_collided()
                        obj.is_colliding = True
                
                elif (obj.is_colliding):
                    obj.stopped_colliding()
                    obj.is_colliding = False

                pygame.draw.rect(util.screen, "white", (collider.pos[0], collider.pos[1], collider.shape[0], collider.shape[1]))
            except:
                pass

        obj.draw()


    pygame.display.flip()

    util.dt = clock.tick(60) / 1000

pygame.quit()