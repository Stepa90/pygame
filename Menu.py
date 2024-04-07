import pygame
pygame.init()

W, H = 600, 400

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

pygame.display.set_caption('Kapetc')
clock = pygame.time.Clock()

bg = pygame.image.load('Images/bg.jpg') #загрузить фон

flRunning = True
FPS = 45


while flRunning:
    sc.blit(bg, (0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('button -', event.button)
            if event.button == 1 and event.pos[0] >= 200 and event.pos[1] >= 90 and event.pos[0] <= 400 and event.pos[1] <= 130:
                print('play')
            if event.button == 1 and event.pos[0] >= 200 and event.pos[1] >= 145 and event.pos[0] <= 400 and event.pos[1] <= 185:
                print('setting')
            if event.button == 1 and event.pos[0] >= 200 and event.pos[1] >= 200 and event.pos[0] <= 400 and event.pos[1] <= 240:
                print('custom')
            if event.button == 1 and event.pos[0] >= 200 and event.pos[1] >= 255 and event.pos[0] <= 400 and event.pos[1] <= 295:
                pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            print('Mouse -', event.pos)

    if not flRunning:
        pygame.quit()
    
    clock.tick(FPS)

print('Программа была остановлена!')