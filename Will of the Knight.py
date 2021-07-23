import pygame, sys
from pygame import Surface, sprite
from pygame import image
from pygame.cursors import arrow
from pygame.draw import rect
from pygame.mixer import stop # import pygame and sys
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('Chippy-music1.wav')
pygame.mixer.music.play()
BPM = 700
footstep = pygame.mixer.Sound('StepArmor1.wav')
jump = pygame.mixer.Sound('Whip1.wav')

clock = pygame.time.Clock() # set up the clock

from pygame.locals import * # import pygame modules
pygame.init() # initiate pygame

pygame.display.set_caption('Pygame Window') # set the window name

WINDOW_SIZE = (1280,1024) # set up window size

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen

display = pygame.Surface((300, 200))

left = False
right = False
stand = True
Arrows = []
health = 100
health_b = 0.62 * health
animationCount = 0

backgroundimage = pygame.image.load('background_image.png')
bigtable = pygame.image.load('bigtable.png')
bochka = pygame.image.load('bochka.png')
metal_box = pygame.image.load('metalbox.png')
purplepicture = pygame.image.load('purplepicture.png')
bottle = pygame.image.load('bottle.png')
bigflag = pygame.image.load('bigflag.png')
mediumflag = pygame.image.load('mediumflag.png')
smallflag = pygame.image.load('smallflag.png')
commonchest = pygame.image.load('commonchest.png')
avatarka = pygame.image.load('avatarka.png')
healthbar = pygame.image.load('healthbar.png')
box = pygame.image.load('box.png')
grass = [pygame.image.load('biggrass1.png'), 
pygame.image.load('biggrass2.png'), 
pygame.image.load('littlegrass1.png'), 
pygame.image.load('littlegrass2.png'), 
pygame.image.load('littlegrass3.png'), 
pygame.image.load('littlegrass4.png'), 
pygame.image.load('littlegrass5.png'), 
pygame.image.load('mediumgrass1.png'), 
pygame.image.load('mediumgrass2.png')]

def draw_hud():
    global health
    health_b = 0.62 * health
    display.blit(avatarka, (5, 3))
    display.blit(healthbar, (23, 3))
    pygame.draw.rect(display, (200, 0, 0), (24, 4, health_b, 10.5))

player_image = [pygame.image.load('adventurer-idle-00.png'), 
pygame.image.load('adventurer-idle-01.png'), 
pygame.image.load('adventurer-idle-02.png'), 
pygame.image.load('adventurer-idle-03.png')]

player_die = [pygame.image.load('adventurer-die-00.png'), 
pygame.image.load('adventurer-die-01.png'), 
pygame.image.load('adventurer-die-02.png'), 
pygame.image.load('adventurer-die-03.png'), 
pygame.image.load('adventurer-die-04.png'), 
pygame.image.load('adventurer-die-06.png')]

player_imageinv = [pygame.image.load('adventurer-idleinv-00.png'), 
pygame.image.load('adventurer-idleinv-01.png'), 
pygame.image.load('adventurer-idleinv-02.png'), 
pygame.image.load('adventurer-idleinv-03.png')]

player_jump_right = [pygame.image.load('adventurer-jump-00.png'), 
pygame.image.load('adventurer-jump-01.png'), 
pygame.image.load('adventurer-jump-02.png'), 
pygame.image.load('adventurer-jump-03.png')]

player_fall_right = [pygame.image.load('adventurer-fall-00.png'), 
pygame.image.load('adventurer-fall-01.png')]

player_jump_left = [pygame.image.load('adventurer-jumpinv-00.png'), 
pygame.image.load('adventurer-jumpinv-01.png'), 
pygame.image.load('adventurer-jumpinv-02.png'), 
pygame.image.load('adventurer-jumpinv-03.png')]

player_fall_left = [pygame.image.load('adventurer-fallinv-00.png'), 
pygame.image.load('adventurer-fallinv-01.png')]

player_run_right = [pygame.image.load('adventurer-run-00.png'), 
pygame.image.load('adventurer-run-01.png'), 
pygame.image.load('adventurer-run-02.png'), 
pygame.image.load('adventurer-run-03.png'), 
pygame.image.load('adventurer-run-04.png')]

player_run_left = [pygame.image.load('adventurer-runinv-00.png'), 
pygame.image.load('adventurer-runinv-01.png'), 
pygame.image.load('adventurer-runinv-02.png'), 
pygame.image.load('adventurer-runinv-03.png'), 
pygame.image.load('adventurer-runinv-04.png')]

player_jump_right = [pygame.image.load('adventurer-jump-00.png'), 
pygame.image.load('adventurer-jump-01.png'), 
pygame.image.load('adventurer-jump-02.png'), 
pygame.image.load('adventurer-jump-03.png')]

player_sword_draw = [pygame.image.load('adventurer-swrd-drw-00.png'), 
pygame.image.load('adventurer-swrd-drw-01.png'), 
pygame.image.load('adventurer-swrd-drw-02.png'), 
pygame.image.load('adventurer-swrd-drw-03.png')]

player_idle_sword = [pygame.image.load('adventurer-idle-2-00.png'), 
pygame.image.load('adventurer-idle-2-01.png'), 
pygame.image.load('adventurer-idle-2-02.png'), 
pygame.image.load('adventurer-idle-2-03.png')]

player_idleinv_sword = [pygame.image.load('adventurer-idle-2-00.png'), 
pygame.image.load('adventurer-idleinv-2-01.png'), 
pygame.image.load('adventurer-idle-2-02.png'), 
pygame.image.load('adventurer-idle-2-03.png')]

player_sword_hide = [pygame.image.load('adventurer-swrd-shte-00.png'), 
pygame.image.load('adventurer-swrd-shte-01.png'), 
pygame.image.load('adventurer-swrd-shte-02.png'), 
pygame.image.load('adventurer-swrd-shte-03.png')]

player_sliding_right = [pygame.image.load('adventurer-slide-00.png'), 
pygame.image.load('adventurer-slide-01.png')]

player_sliding_left = [pygame.image.load('adventurer-slideinv-00.png'), 
pygame.image.load('adventurer-slideinv-01.png')]

archer_idle = [pygame.image.load('archer-idleinv-1.png'), 
pygame.image.load('archer-idleinv-2.png'), 
pygame.image.load('archer-idleinv-3.png'), 
pygame.image.load('archer-idleinv-4.png'), 
pygame.image.load('archer-idleinv-5.png'), 
pygame.image.load('archer-idleinv-6.png')]

default_sword_image = pygame.image.load('default_sword.png')

wood_image = pygame.image.load('wood.png')

sand_image = pygame.image.load('sand.png')

stop_block = pygame.image.load('stop.png')

stone_image = pygame.image.load('cobblestone.png')

bg_image = pygame.image.load('background.png')

grass_image = pygame.image.load('dirtgr.png')

arrow_image = pygame.image.load('arrow.png')

TILE_SIZE = grass_image.get_width()

dirt_image = pygame.image.load('dirt.png')

level = 1
ikl=0
game_level1 = [['5','5','5','5','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['6','6','6','5','5','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['6','6','6','6','5','5','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['6','6','6','6','6','5','5','5','5','5','5','5','5','5','5','5','0','0','0'],
               ['5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','0','0'],
               ['6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','5','5','5','0'],
               ['6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','5','5','5'],
               ['6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','5'],
               ['6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6'],
               ['6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6'],
               ['6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6'],
               ['5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5']]


game_level2 = [['0','0','0','0','0','0','0','0','0','0','0','0','5','5','5','6','5','5','5'],
               ['0','0','0','0','0','0','0','0','0','0','0','5','5','6','6','6','6','6','6'],
               ['0','0','0','0','0','0','0','0','0','0','5','5','6','6','6','6','6','6','6'],
               ['0','0','0','0','0','0','0','0','0','5','5','6','6','6','6','6','6','6','6'],
               ['0','0','0','0','0','0','0','0','5','5','5','5','5','5','5','5','5','5','5'],
               ['0','0','0','0','0','0','0','5','5','6','6','6','6','6','6','6','6','6','6'],
               ['0','0','0','0','0','0','5','5','5','6','6','6','6','6','6','6','6','6','6'],
               ['0','0','0','0','0','5','5','6','6','6','6','6','6','6','6','6','6','6','6'],
               ['0','0','0','0','5','5','6','6','6','6','6','6','6','6','6','6','6','6','6'],
               ['0','0','0','0','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6'],
               ['0','0','0','0','6','6','6','6','6','6','6','6','6','6','6','6','6','6','6'],
               ['2','2','2','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5','5']]


game_level3 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['5','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['5','5','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['5','5','5','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['6','6','6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
               ['6','6','6','0','0','0','0','0','0','0','0','0','0','0','2','2','2','1','1'],
               ['5','5','5','2','2','2','2','2','2','2','2','2','2','2','1','1','1','1','1']]


game_level4 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','3','0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['5','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['5','5','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['5','5','5','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['6','6','6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['6','6','6','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['5','5','5','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2']]


game_level5 = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','8','8','8','0','0','0','0','0','0','0','0','0','0','0','0'],
               ['0','0','0','0','6','6','6','0','0','0','0','8','8','0','0','8','8','8','0'],
               ['0','0','0','0','6','6','6','0','0','0','0','6','6','0','0','6','6','6','0'],
               ['8','8','0','0','6','6','6','0','0','0','0','6','6','0','0','6','6','6','0'],
               ['6','6','0','0','6','6','6','0','0','0','0','6','6','0','0','6','6','6','0'],
               ['6','6','0','0','6','8','8','8','8','0','0','6','6','0','0','6','8','8','8'],
               ['6','6','0','0','6','6','6','6','6','0','0','6','8','8','0','6','6','6','6'],
               ['2','2','2','0','6','6','6','6','6','0','0','6','6','6','0','6','6','6','6'],
               ['1','1','1','2','6','6','6','6','6','0','0','6','6','6','0','6','6','6','6'],
               ['1','1','1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2']]


def collision_test(rect, tiles, Arrows):
    global health
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    for arrow in Arrows:
        if rect.colliderect(arrow):
            health -= 25
            arrow.kill()
    if health <=0:
        pass
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles, Arrows)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.rect.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.rect.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles, Arrows)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.rect.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.rect.bottom
            collision_types['top'] = True
    return rect, collision_types


def idle_animation():
    global animationCount
    if stand:
        if animationCount + 1 >= 30:
            animationCount = 0
            display.blit(player_image[animationCount // 5], (x, y))
            animationCount += 1

moving_right = False
moving_left = False
slide = False
lastMove = 'r'
slideCount = 0

player_y_momentum = 0
air_timer = 0

player_rect = pygame.Rect(105, 140, player_image[0].get_width(), player_image[0].get_height())
archer_rect = pygame.Rect(105, 140, archer_idle[0].get_width(), archer_idle[0].get_height())

def game_level_1():
    tile_rects = []
    y = 0
    for row in game_level1:
        x = 0
        for tile in row:
            if tile == '1':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '2':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '3':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(wood_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '4':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(sand_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '5':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(stone_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '6':
                display.blit(bg_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '7':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(default_sword_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '8':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(box, (x * TILE_SIZE, y * TILE_SIZE))
            x += 1
        y += 1
    return tile_rects

def game_level_2():
    tile_rects = []
    y = 0
    for row in game_level2:
        x = 0
        for tile in row:
            if tile == '1':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '2':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '3':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(wood_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '4':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(sand_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '5':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(stone_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '6':
                display.blit(bg_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '7':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(default_sword_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '8':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(box, (x * TILE_SIZE, y * TILE_SIZE))
            x += 1
        y += 1
    return tile_rects

def game_level_3():
    tile_rects = []
    y = 0
    for row in game_level3:
        x = 0
        for tile in row:
            if tile == '1':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '2':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '3':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(wood_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '4':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(sand_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '5':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(stone_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '6':
                display.blit(bg_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '7':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(default_sword_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '8':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(box, (x * TILE_SIZE, y * TILE_SIZE))
            x += 1
        y += 1
    return tile_rects

def game_level_4():
    tile_rects = []
    y = 0
    for row in game_level4:
        x = 0
        for tile in row:
            if tile == '1':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '2':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '3':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(wood_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '4':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(sand_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '5':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(stone_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '6':
                
                display.blit(bg_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '7':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                tile_rects.append(pf)
                display.blit(default_sword_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '8':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(box, (x * TILE_SIZE, y * TILE_SIZE))
            x += 1
        y += 1
    return tile_rects
class Platform(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = Surface((16, 16))
        self.rect = Rect(x,y, 16, 16)
def game_level_5():
    tile_rects = []
    y = 0
    for row in game_level5:
        x = 0
        for tile in row:
            if tile == '1':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '2':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '3':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(wood_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '4':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(sand_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '5':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(stone_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '6':

                display.blit(bg_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '7':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(default_sword_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '8':
                pf=Platform(x * TILE_SIZE,y * TILE_SIZE)
                pf.image = dirt_image
                tile_rects.append(pf)
                display.blit(box, (x * TILE_SIZE, y * TILE_SIZE))
            #if tile != '0' and tile != '6':
                
                #tile_rects.append(Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1
    return tile_rects
jumping = False

Arrows = []



class Arrow(sprite.Sprite):
    def __init__(self,x,y, dmg, lastdir):
        sprite.Sprite.__init__(self)
        self.yvel = 0
        self.xvel = 5
        self.flag = False
        self.dir=lastdir
        if self.dir == 'l':
            self.xvel = -self.xvel
        if self.dir == 'r':
            self.xvel = self.xvel
        self.image = Surface ((10, 10))
        self.image = arrow_image
        self.image= pygame.transform.rotate(self.image,135)
        self.rect = Rect(x+10+self.xvel, y+20, 10, 10)
        self.dmg = dmg
        self.onGround = False

    def kill(self):
        global Arrows
        for ar in Arrows:
            if ar == self:
                Arrows.pop(Arrows.index(ar))


    def ar_update(self, tile_rects, Arrows):
        self.rect.x += self.xvel
        self.ar_collide(tile_rects, Arrows)
        if self.flag == True:
            if self.onGround == False:
                self.rect.y += self.yvel
                self.ar_collide(tile_rects, Arrows)
        self.draw()
    
    def ar_collide(self, tile_rects, Arrows):
        for tile in tile_rects:
            if sprite.collide_rect(self, tile):
                self.kill()
                self.xvel = 0
                self.yvel = 0.35
                self.flag = True
    
    def draw (self):
        display.blit(self.image, (self.rect.x, self.rect.y))

while True: # game loop
    display.blit(backgroundimage, (0, -10))
    tile_rects = []
    if level == 1:
        tile_rects = game_level_1()
        display.blit(bigtable, (20, 160))
        display.blit(bochka, (70, 160))
        display.blit(bochka, (18, 48))
        display.blit(bochka, (2, 48))
        display.blit(bochka, (86, 160))
        display.blit(metal_box, (64, 48))
        display.blit(metal_box, (64, 32))
        display.blit(metal_box, (48, 48))
        display.blit(metal_box, (48, 32))
        display.blit(metal_box, (32, 48))
        display.blit(purplepicture, (30, 130))
        display.blit(smallflag, (220, 80))
        display.blit(mediumflag, (204, 80))
        display.blit(bigflag, (124, 80))
        display.blit(mediumflag, (140, 80))
        display.blit(smallflag, (156, 80))
        display.blit(mediumflag, (172, 80))
        display.blit(bigflag, (188, 80))
        display.blit(mediumflag, (108, 80))
        display.blit(smallflag, (92, 80))
        display.blit(mediumflag, (76, 80))
        display.blit(bigflag, (60, 80))
        display.blit(smallflag, (44, 80))
        display.blit(mediumflag, (28, 80))
        display.blit(smallflag, (12, 80))
        display.blit(bigflag, (-4, 80))
        display.blit(commonchest, (-25, 48))
    elif level == 2:
        display.blit(backgroundimage, (-200, -60))
        tile_rects = game_level_2()
    elif level == 3:
        display.blit(backgroundimage, (-100, -60))
        tile_rects = game_level_3()
    elif level == 4:
        tile_rects = game_level_4()
    elif level == 5:
        tile_rects = game_level_5()
        display.blit(archer_idle[animationCount // 10], (245, 6))
        display.blit(archer_idle[animationCount // 10], (260, 70))
    player_movement = [0, 0]
    if moving_right:
        player_movement[0] += 2
    if moving_left:
        player_movement[0] -= 2
        pygame.mixer.Sound.play(footstep)
    player_movement[1] += player_y_momentum
    player_y_momentum += 0.45
    if player_y_momentum > 3:
        player_y_momentum = 3
    if slide:
        if lastMove == 'r':
            player_movement[0] += 2.5
        else:
            player_movement[0] -= 1.5
    
    player_rect, collisions = move(player_rect, player_movement, tile_rects)

    if collisions['bottom']:
        player_y_momentum = 0
        jumping = False
        air_timer = 0
    else:
        air_timer += 1
    if ikl+1>=60 and level== 5 and health>0:
        ar=Arrow(245, 6, 35,"l")
        Arrows.append (ar)
        ar=Arrow(260, 70, 35, "l")
        Arrows.append (ar)
        ikl=0
    ikl+=1
    if animationCount + 1 >= 60:
        animationCount = 0
        
    for ar in Arrows:
        ar.ar_update(tile_rects, Arrows)
    if not slide:
        for event in pygame.event.get(): # event loop
            if event.type == QUIT: # check for window quit
                pygame.quit() # stop pygame
                sys.exit() # stop script
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    moving_right = True
                    lastMove = 'r'
                if event.key == K_LEFT:
                    moving_left = True
                    lastMove = 'l'
                if event.key == K_UP:
                    pygame.mixer.Sound.play(jump)
                    jumping = True
                    animationCount = 0
                    if air_timer < 6:
                        player_y_momentum = -5.9
                if event.key == K_RIGHT:
                    moving_right = True
                if event.key == K_DOWN:
                    slide = True
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False
        if jumping:
            if player_y_momentum > 0:
                if lastMove == 'r':
                    display.blit(player_fall_right[animationCount // 30], (player_rect.x, player_rect.y))
                    if health <=0:
                        break
                else:
                    display.blit(player_fall_left[animationCount // 30], (player_rect.x, player_rect.y))
                    if health <=0:
                        break
            else:
                if lastMove == 'r':
                    display.blit(player_jump_right[animationCount // 15], (player_rect.x, player_rect.y))
                    if health <=0:
                        break
                else:
                    display.blit(player_jump_left[animationCount // 15], (player_rect.x, player_rect.y))
                    if health <=0:
                        break
                if air_timer < 6:
                    if lastMove == 'r':
                        display.blit(player_fall_right[animationCount // 30], (player_rect.x, player_rect.y))
                    else:
                        display.blit(player_fall_left[animationCount // 30], (player_rect.x, player_rect.y))
            animationCount += 1            
        elif moving_left:
            display.blit(player_run_left[animationCount // 12], (player_rect.x, player_rect.y))
            if health <=0:
                break
            animationCount += 1
        elif moving_right:
            display.blit(player_run_right[animationCount // 12], (player_rect.x, player_rect.y))
            if health <=0:
                break
            animationCount += 1
        elif health <=0:
            display.blit(player_die[animationCount // 10], (player_rect.x, player_rect.y))
        else:
            if lastMove == 'l':
                display.blit(player_imageinv[animationCount // 15], (player_rect.x, player_rect.y))
                if health <=0:
                    break
                animationCount += 1
            else: 
                display.blit(player_image[animationCount // 15], (player_rect.x, player_rect.y))
                if health <=0:
                    break
                animationCount += 1
    else:
        player_rect = pygame.Rect(player_rect.x, player_rect.y, player_sliding_right[0].get_width(), player_sliding_right[0].get_height())
        if lastMove == 'r':
            display.blit(player_sliding_right[animationCount // 30], (player_rect.x, player_rect.y))
        else:
            display.blit(player_sliding_left[animationCount // 30], (player_rect.x, player_rect.y))
        slideCount += 1
        if slideCount > 30:
            player_rect = pygame.Rect(player_rect.x, player_rect.y, player_image[0].get_width(), player_image[0].get_height())
            slideCount = 0
            slide = False
            animationCount += 1
    
    if level == 1:
        if player_rect.x <= 15 and player_rect.y <=145 and player_rect.y >=145:
            level = 2
            player_rect.x = 260
            player_rect.y = 145
    if level == 1:
        if player_rect.x >= 277 and player_rect.y <= 145 and player_rect.y >=145:
            level = 3
            player_rect.x = 25
            player_rect.y = 145
    if level == 1:
        if player_rect.x >= 277 and player_rect.y <= 80:
            level = 3
            player_rect.x = 15
            player_rect.y = 60
    if level == 1:
        if player_rect.x <= 60 and player_rect.y <= 40:
            level = 3
            player_rect.x = 100
            player_rect.y = 60
    if level == 2:
        if player_rect.x >= 270 and player_rect.y <= 145 and player_rect.y >=145:
            level = 1
            player_rect.x = 15
            player_rect.y = 145
    if level == 3:
        if player_rect.x <= 15 and player_rect.y <= 145 and player_rect.y >=145:
            level = 1
            player_rect.x = 275
            player_rect.y = 145
    if level == 3:
        if player_rect.x <= 25 and player_rect.y == 110:
            level = 1
            player_rect.x = 200
            player_rect.y = 60
    if level == 3:
        if player_rect.x >= 260 and player_rect.y <= 145 and player_rect.y >=100:
            
            player_rect.x = 15
            player_rect.y = 125
            display.blit(player_sword_draw[animationCount // 15], (player_rect.x, player_rect.y))
            animationCount = 0
            level = 5
            
            tile_rects = game_level_5()
            
    if level == 4:
        pass
    if level == 5:
        if player_rect.x <= 5 and player_rect.y <= 145 and player_rect.y >=100:
            level = 3
            player_rect.x = 250
            player_rect.y = 100
    draw_hud()
    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update() # update display
    clock.tick(60) # maintain 60 fps