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
def escape_event():
    global running
    running = False

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            escape_event()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                escape_event()
def escape_event():
    global running
    running=False



def moving_character(p1,p2):
      x1, y1 = p1[0], p1[1]
      x2, y2 = p2[0], p2[1]
      a = (y2-y1)/(x2-x1)
      b = y1 - x1 * a
      if(x1<x2):
          for x in range(x1, x2 + 1, 10):
              moving_right() 
              y = a * x + b
      



def right_events():
    pass

def left_events():
    pass

def moving_right():
    global frame
    global x
    x += dirx * 5
    if x>790:
        x=790
    frame = (frame + 1) % 4
    character.clip_draw(frame * 160, 4 + 640, 160, 160, x, y, 100, 100)
    update_canvas()
def moving_left():
    global frame
    global x
    x += dirx * 5
    if x<10:
        x=10
    frame = (frame + 1) % 4
    character.clip_draw(frame * 160, 4 + 320, 160, 160, x, y, 100, 100)
def moving_up():
    pass


def draw_hand():
    global randomPoints_X,randomPoints_Y
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(randomPoints_X,randomPoints_Y)
    update_canvas()

while running:
    handle_events()
    draw_hand()
    moving_right()

    delay(0.05)