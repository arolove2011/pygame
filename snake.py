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
CORAl= (255, 102, 102)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 222)
RED = (153, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
        self.length = 2
        self.positions = [(int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP< DOWN, LEFT, RIGHT])


    #뱀 방향 조정
    def control(self, xy):
        if (xy[0] * -1, xy[1] * -1) == self.direction:
            return
        else:
            self.direction = xy

    #뱀 이동
    def move(self):
        cur = self.positions[0]
        x, y = self.direction
        new = (cur[0]+(x*GRID_SIZE), (cur[1]+(y*GRID_SIZE)))

        #뱀이 자기 몸통에 닿았을 경우 뱀 처음부터 다시 생성
        if new in self.positions[2:]:
            sleep(1)
            self.create()

        #뱀이 게임 화면을 넘어갈 경우 뱀 처음부터 다시 생성
        elif new[0] < 0 or new[0] >= SCREEN_WIDTH or \
                new[1] < 0 or new[1] >= SCREEN_WIDTH:
            sleep(1)
            self.create()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def eat(self):
        self.length += 1
    def draw(self, screen):
        red, green, blue = 50 / (self.length - 1), 150, 150 / (self.length - 1)
        for i, p in enumerate(self.positions):
            color = (100 + red * i, green, blue * 1)
            rect = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, color, rect)

class Feed():
    def __init__(self):
        self.positions = (0, 0)
        self.color = CORAl
        self.create()

    #먹이 생성
    def create(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        self.position = x * GRID_SIZE, y * GRID_SIZE

    #먹이 그리기
    def draw(self, screen):
        rect = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.color, rect)

#함정 객체
class Trap():
    def __init__(self):
        self.positions = (0, 0)
        self.color = RED
        self.create()

    #함정 생성
    def create(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        self.position = x * GRID_SIZE, y * GRID_SIZE

    #함정 그리기
    def draw(self, screen):
        circle = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.circle(screen, self.color, circle)



#게임 객체
class Game():
    def __init__(self):
        self.snake = Snake()
        self.feed = Feed()
        self.feed2 = Feed()
        self.trap = Trap()
        self.speed = 200

    #게임 이벤트 처리 및 조작
    def process_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.control(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.control(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.control(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.control(RIGHT)
        return False
    
    #게임 로직 수행
    def run_logic(self):
        self.snake.move()
        self.check_eat(self.snake, self.feed)
        self.check_eat(self.snake, self.feed2)
        self.speed = (20 + self.snake.length) / 4

    #뱀이 먹이를 먹었는지 체크
    def check_eat(self, snake, feed):
        if snake.positions[0] == feed.position:
            snake.eat()
            feed.create()

    #뱀이 함정에 닿은면 체크-
    def check_reach(self, snake, trap):
        if snake.positions[0]== trap.position:
            font = pygame.font.SysFont('Gulim', 40, True, False)
            text = font.render("Game Over", True, BLACK)
            screen.blit(text, [200, 600])
            



    #게임 정보 출력
    def draw_info(self, length, speed, screen):
        info = "뱀의 길이: " + str(length) + "   " + "뱀의 속도: " + str(round(speed, 4))
        font = pygame.font.SysFont('Gulim', 30, False, False)
        text_obj = font.render(info, True, BLACK)
        text_rect = text_obj.get_rect()
        text_rect.x, text_rect.y = 10, 10
        screen.blit(text_obj, text_rect)

    #게임 프레임 처리
    def display_frame(self, screen):
        screen.fill(YELLOW)
        self.draw_info(self.snake.length, self.speed, screen)
        self.snake.draw(screen)
        self.feed.draw(screen)
        self.feed2.draw(screen)
        screen.blit(screen, (0, 0))



def main():
    #게임 초기화 및 환경 설정
    pygame.init()
    pygame.display.set_caption('뱀 게임')
    clock = pygame.time.Clock()
    game = Game()

    done = False
    while not done:
        done = game.process_event()
        game.run_logic()
        game.display_frame(screen)
        pygame.display.flip()
        clock.tick(game.speed)


    pygame.quit()

if __name__ == '__main__':
    main()