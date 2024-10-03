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
randomPoints_X=random.randint(50,TUK_WIDTH-50)
randomPoints_Y=random.randint(50,TUK_HEIGHT-50)
speed = 5  
direction = 1  # 1: 오른쪽, -1: 왼쪽


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



def moving_character(p1, p2):
    global x, y, frame, direction, randomPoints_X, randomPoints_Y

    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx**2+dy**2)

    if distance == 0:
        return

    # 단위 벡터 계산
    dx = dx/distance
    dy = dy/distance
    move_x = dx * speed
    move_y = dy * speed

    # 다음 위치 계산
    new_x = x + move_x
    new_y = y + move_y

    # 손에 도착했을 때 처리
    if math.sqrt((x2 - new_x)**2+(y2 - new_y)**2) < speed:
        x, y = x2, y2
        randomPoints_X = random.randint(50, TUK_WIDTH - 50)
        randomPoints_Y = random.randint(50, TUK_HEIGHT - 50)
    else:
        x = new_x
        y = new_y

    # 이동 방향에 따라 캐릭터의 바라보는 방향 설정
    if move_x > 0:
        direction = 1  # 오른쪽
    elif move_x < 0:
        direction = -1  # 왼쪽

 
    frame = (frame + 1) % 8
      
def draw_character():
    global frame, direction, x, y
    if x<randomPoints_X:
        direction=1
    elif x>randomPoints_X:
        direction=-1

    if direction==1: #오른쪽
        moving_character([x,y],[randomPoints_X,randomPoints_Y])
        character.clip_draw(frame * 50, 104 , 100,100, x, y, 100, 100)
    elif direction==-1:
        moving_character([x,y],[randomPoints_X,randomPoints_Y])
        character.clip_draw(frame * 50, 4 , 100,100, x, y, 100, 100)







def draw_hand():
    hand.draw(randomPoints_X,randomPoints_Y)

while running:
    handle_events()
    moving_character([x, y], [randomPoints_X, randomPoints_Y])
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    draw_hand()
    draw_character()
    update_canvas()

    delay(0.05)