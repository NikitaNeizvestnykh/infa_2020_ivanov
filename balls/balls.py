import pygame
from random import randint
pygame.font.init()
text = pygame.font.Font(None, 24)

collors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 0)]

clock = pygame.time.Clock()

def new_ball():
    x = randint(100, 900)
    y = randint(100, 900)
    r = randint(10, 50)
    collor = collors[randint(0, 2)]
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    h_ball = (x, y, r, collor, vx, vy)
    return h_ball

def ball(h):
    x, y, r, collor, vx, vy = h
    x += vx
    y += vy
    if x + vx + r >= 1000 or x + vx - r <= 0:
        vx *= -1
    if y + vy + r >= 1000 or y + vy - r <= 0:
        vy *= -1
    return (x, y, r, collor, vx, vy)

def prove(h, xy):
    x, y = xy
    x1, y1, r, collor, vx, vy, = h
    if (x-x1)**2+(y-y1)**2<=r**2:
        return True
    return False

screen = pygame.display.set_mode((1000, 1000))
n = 10

gg = [new_ball() for i in range(n)]
pygame.display.update()
k = 0
finished = True
while finished:
    clock.tick(30)
    #g = ball(g)
    gg = [ball(x) for x in gg]
    for g in gg:
        pygame.draw.circle(screen, g[3], (g[0], g[1]), g[2])

    sms = text.render('Количество очков: '+str(k), True, (180, 0, 0))
    screen.blit(sms, (20, 20))
    pygame.display.update()
    screen.fill(collors[-1])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            xy = event.pos
            for i in range(n):
                g = gg[i]
                if prove(g, xy):
                    k += 1
                    gg[i] = (0, 0, 0, (0, 0, 0), 0, 0)
