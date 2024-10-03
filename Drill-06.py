from pico2d import *
import random


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand=load_image('hand_arrow.png')


running=True
frame=0
dirx=0
diry=0
randomPoints_X=random.randint(0,TUK_WIDTH)
randomPoints_Y=random.randint(0,TUK_HEIGHT)

def handl_events():
    pass

def moving_right():
    pass
def moving_left():
    pass
def moving_up():
    pass
def draw_hand():
    pass

while True:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(randomPoints_X,randomPoints_Y)
    update_canvas()