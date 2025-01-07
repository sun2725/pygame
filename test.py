import pygame

pygame.init()

background = pygame.display.set_mode((480,360))
pygame.display.set_caption("game 01")

x_pos = background.get_size()[0] // 2
y_pos = background.get_size()[1] // 2

to_x = 0
to_y = 0

play = True
while play : 
    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y = -0.1
            elif event.key == pygame.K_DOWN:
                to_y = 0.1
            elif event.key == pygame.K_LEFT:
                to_x = -0.1
            elif event.key == pygame.K_RIGHT:
                to_x = 0.1
            elif event.key == pygame.K_SPACE:
                y_pos -= 10
            elif event.key == pygame.K_a:
                print("a")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                to_y = 0
            elif event.key == pygame.K_DOWN:
                to_y = 0
            elif event.key == pygame.K_LEFT:
                to_x = 0
            elif event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_SPACE:
                y_pos += 10

        if event.type == pygame.QUIT :
            play = False
    x_pos += to_x
    y_pos += to_y

    background.fill((74,189,214))
    pygame.draw.circle(background, (255,255,255), (x_pos, y_pos), 5)
    pygame.display.update()

pygame.quit()