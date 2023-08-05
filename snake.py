import pygame
import os
import sys
import random
from time import sleep

#게임 스크린 전역 변수
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

##게임 화면 전역 변수
GRID_SIZE = 20
GRID_WIDTH= SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT/ GRID_SIZE

#색상 전역변수
WHITE = (255, 255, 255)
ORANGE = (250, 150, 0)
GRAY = (100, 100, 100)

#방향 전역변수
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1,0)

#뱀 객체
class Snake():
    def __init__(self):
        self.create()
    #뱀 생성
    def create(self):
        self.lenth = 2
        self.positions = [(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP< DOWN, LEFT, RIGHT])
    def control(self, xy):
        if (xy[0] * -1, xy[1] * -1) == self.sirection:
            return
        else:
            self.direction = xy

    #뱀 이동
    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (cur[0] + (x * GRID_SIZE)), (cur[1] + (y * GRID_SIZE))

        #뱀이 자기 몸통에 닿았을 경우 뱀 처음부터 다시 생성
        if new in self.positions[2:]:
            sleep(1)
            self.create()
        #뱀이 게임 화면을 넘어갈 경우 뱀 처음부터 다시 생성
        elif new[0] < 0 or new[0] >= SCREEN_WIDTH or \
                new[1] < 0 or new[1] >= SCREEN_WIDTH:
            sleep(1)
            self.create()

def main():
    pygame.init()
    pygame.display.set_caption('Snake Game')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = game()

    done = False
    while not done:
        screen.fill(WHITE)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()
