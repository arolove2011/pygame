import pygame
import os
import sys
import random
from time import sleep

# 게임 스크린 전역변수
screen_width = 480
screen_height = 800

# 색상 전역변수
black = (0, 0, 0)
white = (255,255,255)
gray = (150, 150,150)
red = (200, 0, 0)

# 게임 전역 변수 
car_c = 3
lane_count = 5
speed = 10

class Lane():
    def __init_(self):
        self.color = white
        self.width = 10
        self.height = 80
        self.gap = 20
        self.space= (screen_width - (self.width*lane_count)) / (lane_count -1)
        self.count = 10
        self.x = 0
        self.y = - self.height
    def move(self, speed, screen):
        self.y += speed
        if self.y > 0:
            self.y = -self.height
        self.draw(screen)
    def draw(self, screen):
        next_lane = self.y
        for i in range(self.acount):
            pygame.draw.rect(screen, self.color, (self.x, next_lane, self.width, self.height))
            next_lane += self.height + self.gap
class Car():
    def __init__(self, x=0, y=0, dx=0, dy=0):
        self.x = x
        self.y = y
        self.dx= dx
        self.dy = dy

        car_images_path = resource_path('assets/car')
        image_file_list = os.listdir(car_images_path)
        self.image_path_list = [os.path.join(car_images_path, file) for file in image_file_list if file.endswith(".png")]
        
        crash_image_path = resource_path('assets/crash.png')
        self.crash_image = pygame.mixer.Sound(crash_image_path)

        crash_sound_path = resource_path('assets/crash.wav')
        self.crash_sound = pygame.mixer.Sound(crash_sound_path)

        engine_sound_path = resource_path('assets/engine.wav')
        self.engine_sound = pygame.mixer.Sound(engine_sound_path)

        collision_sound_path = resource_path('assets/collision.wav')
        self.collision_sound = pygame.mixer.Sound(collision_sound_path)

    #자동차 이미지 로드
    def load_image(self):
        choice_car_path = random.choice(self.image_path_list)
        self.image = pygame.image.load(choice_car_path)
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height


    #자동차 로드
    def load(self):
        self.load_image()
        self.x = screen_width //2
        self.y = screen_height - self.height
        self.dx = 0
        self.dy = 0
        self.engine_sound.play()

    #자동차 랜덤 로드
    def load_random(self):
            self.load_image()
            self.x = random.randrange(0, screen_width - self.width)
            self.y = 0 - self.height
            self.dx = 0
            self.dy = random.randint(5, 10)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    #스크린 범위 체크
    def out_of_screen(self):
        if self.x < 0 or self.x > screen_width-self.width:
            self.x -= self.dx
        if self.y <0 or self.y > screen_height-self.height:
            self.y -= self.dy

    def check_crash(self, car):
        if (self.x+self.width >car.x) and (self.x < car.x + car.width) and (self.y < car.y + car.height) and (self.y + self.height):
            return True
        else:
            return False
        
    # 자동차 그리기
    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y])

    # 자동차 충돌 그리기
    def draw_crash(self, screen):
        width = self.crash_image.get_rect().width
        height = self.crash_image.get_rect().height
        draw_x = self.x + self.width//2-width / 2
        draw_y = self.y + self.height // 2 - height // 2
        screen.blit(self.crash_image, (draw_x, draw_y))
        pygame.display.update()

class Game():
    def __init__(self):
        menu_image_path = resource_path("assets/menu_car.png")
        self.image_intro = pygame.image.load(menu_image_path)
        pygame.mixer.music.load(resource_path("assets/race.wav"))
        self.font_40 = pygame.font.SysFont("Malgun Gothic", 40)
        self.font_30 = pygame.font.SysFont("Malgun Gothic", 30)

        self.lanes = []
        for i in range(lane_count):
            lane = Lane()
            lane.x = i *int(lane.space+lane.width)
            self.lanes.append(lane)

        self.cars = []
        for i in range(car_c):
            car = Car()
            self.score = 0
            self.menu_on = True

        def process_event(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if self.menu_on:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pygame.mixer.music.play(-1)
                            pygame.mouse.set_visible(False)
                            self.score = 0
                            self.menu_on = False
                            self.player.load()
                            for car in self.cars:
                                car.load_random()
                            sleep(4)
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.player.dy -= 5
                        elif event.key == pygame.K_DOWN:
                            self.player.dy += 5
                        elif event.key == pygame.K_LEFT:
                            self.player.dx -= 5
                        elif event.key == pygame.K_RIGHT:
                            self.player.dx += 5
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            self.player.dy = 0
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            self.player.dx = 0
                return True
            
            def run_logic(self, screen):
                for car in self.cars:
                    if car.y > screen_height:
                        self.score += 10
                        car.load_random()
                        
                    if self.player.check.check_crash(car):
                        self.menu_on = True
                        pygame.mixer.music.stop()
                        self.player.crash_sound.play()
                        self.player.draw_crash(screen)
                        car.draw__crash(screen)
                        sleep(1)
                        pygame.mouse.set_visible(True)

                    for com in self.cars:
                        if car == com:
                            pass
                        elif car.check_crash(com):
                            self.score += 10
                            car.collision_sound.play()
                            car.draw_crash(screen)
                            car.load_random()
                            com.draw_crash(screen)
                            com.load_random()
    def draw_text(self, screen, text, font, x, y, main_color):
        text_obj = font.render(text, True, main_color)
        text_rect = text_obj.get_rect()
        text_rect.conter = x, y
        screen.bilt(text_obj, text_rect)
    def display_menu(self, screen):
        screen.fill(gray)
        screen.bilt(self.image_intro, [40, 150])
        draw_x = screen_width//2
        draw_y = screen_height//2
        self.draw.text(screen, "레이싱 게임", self.font_40, draw_x, draw_y+50, black)
        self.draw.text(screen, "점수"+str(self.score), self.font_40, draw_x, draw_y+50, white)
        self.draw.text(screen, "스페이스 키를 눌러 실행하시오", self.font_40, draw_x, draw_y+50, red)

    def display_frame(self, screen):
        screen.fill(gray)
        for lane in self.lanes:
            lane.move(speed, screen)
        self.player.draw(screen)
        self.player.move()
        self.player.out_of_screen()

        for car in self.cars:
            car.draw(screen)
            car.move()

        self.draw_text(screen, "점수:"+str(self.score))
def resource_path(path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, path)

def main():
    pygame.init()
    pygame.display.set_caption("자동차 게임")
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    running = True
    while running:
        running = game.process_event()
        if game.menu_on:
           game.display_menu(screen)
        else:
           game.run_logic(screen)
           game.display_frame(screen)
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
main()