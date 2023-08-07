import pygame
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

pygame.init()

pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#게임 화면 업데이트 속도
clock = pygame.time.Clock()

r_x = int(SCREEN_WIDTH/2)
r_y = int(SCREEN_HEIGHT/2)
r_dx = 0
r_dy = 0



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


#키가 눌릴 경우
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:     
                r_dx = -5
            elif event.key == pygame.K_RIGHT:
                r_dx = 5
            elif event.key == pygame.K_UP:
                r_dy = -5
            elif event.key == pygame.K_DOWN:
                r_dy = 5
        #키가 놓일 경우
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                r_dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                r_dy = 0

    r_x += r_dx
    r_y += r_dy

    screen.fill(WHITE)
    rect = pygame.Rect(r_x, r_y, 20, 20)
    pygame.draw.rect(screen, BLUE, rect, 0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

