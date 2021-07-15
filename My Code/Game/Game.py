import pygame

pygame.init()

win = pygame.display.set_mode((1280, 1024))


pygame.display.set_caption('New Game')

def player_location():
    pass

x = 20
y = 709
width = 60
height = 71
speed = 15

left = False
right = False

animationCount  = 0

platformWithSpikes = pygame.image.load('platform_with_spikes2.png')

platformWithoutSpikes = pygame.image.load('platform_without_spikes.png')

pistol = pygame.image.load('pistol2.png')

walkRight = [pygame.image.load('pygame_right_1.png'),
pygame.image.load('pygame_right_2.png'),
pygame.image.load('pygame_right_3.png'),
pygame.image.load('pygame_right_4.png'),
pygame.image.load('pygame_right_5.png'),
pygame.image.load('pygame_right_6.png')]

walkLeft = [pygame.image.load('pygame_left_1.png'),
pygame.image.load('pygame_left_2.png'),
pygame.image.load('pygame_left_3.png'),
pygame.image.load('pygame_left_4.png'),
pygame.image.load('pygame_left_5.png'),
pygame.image.load('pygame_left_6.png')]

playerStand = pygame.image.load('pygame_idle.png')
bg = pygame.image.load('pygame_bg_pixel.png')

clock = pygame.time.Clock()

def collision():
    pass

def draw_window():
    global animationCount
    win.blit(bg, (0, 0))
    win.blit(platformWithSpikes, (300, 50))
    win.blit(platformWithSpikes, (680, 520))
    win.blit(platformWithSpikes, (220, 300))
    win.blit(platformWithSpikes, (30, 420))
    win.blit(platformWithoutSpikes, (350, 500))
    win.blit(platformWithoutSpikes, (20, 100))
    win.blit(pistol, (50, 50))
    win.blit(platformWithoutSpikes, (960, 100))
    win.blit(platformWithoutSpikes, (1150, 96))
    win.blit(platformWithoutSpikes, (1000, 620))
    win.blit(platformWithoutSpikes, (580, 200))
    if animationCount + 1 >= 30:
        animationCount = 0
    if left:
        win.blit(walkLeft[animationCount // 5], (x, y))
        animationCount += 1
    elif right:
        win.blit(walkRight[animationCount // 5], (x, y))
        animationCount += 1
    else:
        win.blit(playerStand, (x, y))

def draw_window2():
    global animationCount
    win.blit(bg, (0, 0))
    win.blit(platformWithSpikes, (300, 50))
    win.blit(platformWithSpikes, (680, 520))
    win.blit(platformWithSpikes, (220, 300))
    win.blit(platformWithSpikes, (30, 420))
    win.blit(platformWithoutSpikes, (350, 500))
    win.blit(platformWithoutSpikes, (20, 100))
    win.blit(pistol, (50, 50))
    win.blit(platformWithoutSpikes, (960, 100))
    win.blit(platformWithoutSpikes, (1150, 96))
    win.blit(platformWithoutSpikes, (1000, 620))
    win.blit(platformWithoutSpikes, (580, 200))

isJump = False
JumpCount = 10

run = True
while run:
    #pygame.time.delay(5)
    clock.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 9.5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1280 - width - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animationCount = 0
    if not isJump:
        if keys[pygame.K_UP] and y > 5:
            isJump = True
    else:
        if JumpCount >= -10:
            if JumpCount < 0:
                y += (JumpCount ** 2) / 2    
            else:
                y -= (JumpCount ** 2) / 2
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 10    

    win.fill((0,0,0))
    draw_window()

    pygame.display.update()

pygame.quit()











































