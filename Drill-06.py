from pico2d import *
import random


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand=load_image('hand_arrow.png')


running=True
frame=0
x=TUK_WIDTH//2
y=TUK_HEIGHT//2
dirx=0
diry=0
randomPoints_X=random.randint(0,TUK_WIDTH)
randomPoints_Y=random.randint(0,TUK_HEIGHT)

def handle_events():
    pass

def moving_right():
    pass
def moving_left():
    pass
def moving_up():
    pass
def draw_right():
    global frame
    global x
    x += dirx * 5
    if x>790:
        x=790
    frame = (frame + 1) % 4
    character.clip_draw(frame * 160, 4 + 640, 160, 160, x, y, 100, 100)
    update_canvas()

def draw_left():
    global frame
    global x
    x += dirx * 5
    if x<10:
        x=10
    frame = (frame + 1) % 4
    character.clip_draw(frame * 160, 4 + 320, 160, 160, x, y, 100, 100)

def draw_hand():
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(randomPoints_X,randomPoints_Y)
    update_canvas()

while True:
    draw_hand()
    draw_right()

    delay(0.05)