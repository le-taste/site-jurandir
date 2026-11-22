import game_obj
import collision as col
import utility as util
import art
import scene_manager as SM

width = 1000
height = 400
x_center = util.screen_width / 2
y_center = util.screen_height / 2
table = game_obj.game_object(SM.SCENES.DESK)
table.sprite = art.scale_image(art.table, util.screen_width, util.screen_height)

class pc(game_obj.game_object):

    def update(self):
        if util.mouse_pressed and self.is_colliding:
            self.switch_scene()

    def switch_scene(self):
        SM.current_scene = SM.SCENES.PC.value
        
        

pos = (800, 130)
pc_obj = pc(SM.SCENES.DESK, pos[0], pos[1])
pc_obj.sprite = art.scale_image_by_magnitude(art.pc, 0.7)
width = pc_obj.sprite.get_width()
height = pc_obj.sprite.get_height()
pc_obj.collider_list =  col.collider(0, pos, [width, height])