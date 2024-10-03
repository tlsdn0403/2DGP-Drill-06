from pico2d import *
import random
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand=load_image('hand_arrow')

randomPoints=[(random.randint(-500,500),random.randint(-350,350))]

def handl_events():
    pass

def moving_right():
    pass
def moving_left():
    pass
def moving_up():
    pass