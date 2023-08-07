import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()
pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
color = BLACK

running = True
while running:
    for event in pygame.event.get():
        #키가 눌릴 경우
            if event.type == pygame.QUIT:
                Running = False
            elif event.key == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    color = RED
            elif event.key == pygame.K_UP:
                 color = BLACK
    screen.fill(WHITE)
    rect = pygame.Rect(SCREEN_WIDTH/2-25, SCREEN_HEIGHT/2-25, 100, 100)
    pygame.draw.rect(screen, color, rect, 0)
    # pygame.draw.rect(screen, BLUE, rect2, 0)
    # rect4 = pygame.Rect(200, 200, 40, 40)
    # pygame.draw.rect(screen, GREEN, rect4, 0)
    # rect3 = pygame.Rect(200, 200, 20, 20)
    # pygame.draw.rect(screen, RED, rect3, 0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()