import pygame
pygame.init()

W, H = 600, 400

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

stop = True

while stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = False

    sc.fill((255, 255, 255))
    pygame.display.update()

    clock.tick(60)
    if stop == False:
        pygame.quit()

print('Программа была завершена')

'''pygame.display.set_caption('My game')
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.draw.rect(sc, WHITE, (10, 10, 50, 100), 2)
pygame.display.update()

flRunning = True
FPS = 60

x = W // 2
y = H // 2
speed = 5

flLeft = False
flRight = False

while flRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
        #if event.type == pygame.MOUSEBUTTONDOWN:
        #    print('button -', event.button)
        #if event.type == pygame.MOUSEMOTION:
        #    print('Mouse -', event.pos)
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed

    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    pygame.display.update()

    if not flRunning:
        pygame.quit()
    
    clock.tick(FPS)

print('Программа была остановлена!')'''