import pygame
import os
import random


# 색 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (20, 60, 120)
ORANGE = (250, 170, 70)
RED = (250, 0, 0)

# 게임 스크린 크기
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

current_path = os.path.dirname(__name__)
assets_path = os.path.join(current_path, "assets")

#공 객체
class Ball():
    def __init__(self, bounce_sound):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_WIDTH // 2, 12, 12)
        self.bounce_sound = bounce_sound
        self.dx = 0
        self.dy = 5
    
    #공 업데이트
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        
        if self.rect.left<0:
            self.dx *= -1
            self.rect.left = 0
            self.bounce.play()
        
        elif self.rect.right > SCREEN_WIDTH:
            self.dx *= -1
            self.rect.right = SCREEN_WIDTH
            self.bounce_sound.play()
    
    #공 리셋
    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.dx = random.randint(-3, 3)
        self.dy = 5

    # 공 그리기
    def draw(self, screen):
        pygame.draw.rect(screen, ORANGE, self.rect)


# 플레이어 객체
class Player(object):
    def __init__(self, ping_sound):
        self.rect = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 40, 50, 15)
        self.ping_sound = ping_sound
        self.dx = 0

    # 플레이어 업데이트
    def update(self, ball):
        if self.rect.left <= 0 and self.dx < 0:
            self.dx = 0
        elif self.rect.right >= SCREEN_WIDTH and self.dx > 0:
            self.dx = 0

        # 플레이어가 공이랑 충돌한 경우
        if self.rect.colliderect(ball.rect):
            ball.dx = random.randint(-5, 5)
            ball.dy *= -1
            ball.rect.bottom = self.rect.top
            self.ping_sound.play()

        self.rect.x += self.dx

    # 그리기
    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)


#적 객체
class Enemy():
    def __init__(self, pong_sound):
        self.rect = pygame.Rect((SCREEN_WIDTH / 2), 40, 50, 15)
        self.pong_sound = pong_sound

    # 업데이트
    def update(self, ball):

        # 적보다 공이 오른쪽에 있을 때
        if self.rect.centerx < ball.rect.centerx:
            diff = ball.rect.centerx - self.rect.centerx
            if diff <= 4:
                self.rect.centerx = ball.rect.centerx
            else:
                self.rect.x += 4
        # 적보다 공이 왼쪽에 있을 때
        if self.rect.centerx > ball.rect.centerx:
            diff = self.rect.centerx - ball.rect.centerx
            if diff <= 4:
                self.rect.centerx = ball.rect.centerx
            else:
                self.rect.x -= 4


        # 적이 공과 충돌한 경우
        if self.rect.colliderect(ball.rect):
            ball.dy *= -1
            ball.rect.top = self.rect.bottom
            self.pong_sound.play()

    # 그리기
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)

#게임 객체
class Game():
    def __init__(self):
        bounce_sound = pygame.mixer.Sound(os.path.join(assets_path, "bounce.wav"))
        ping_sound = pygame.mixer.Sound(os.path.join(assets_path, "ping.wav"))
        pong_sound = pygame.mixer.Sound(os.path.join(assets_path, "pong.wav"))
        self.font = pygame.mixer.Sound("맑은 고딕", 50, False, False)
        self.ball = Ball(bounce_sound)
        self.player = Player(ping_sound)
        self.enemy = Enemy(pong_sound)
        self.player_score = 0
        self.enemy_score = 0

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.dx -= 5
                elif event.key == pygame.K_RIGHT:
                    self.player.dx += 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.dx = 0
                    
        return True
    def run_logic(self):
        self.ball.update()
        self.player.update(self.ball)
        self.enemy.update(self.ball)



def main():
    pygame.init()
    pygame.display.set_caption("핑퐁게임")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game()

    running = True
    while running:
        running = game.process_events()
        screen.fill(BLUE)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()