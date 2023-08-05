import pygame
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

GRAY = (200, 200, 200)

pygame.init()

pygame.display.set_caption("키보드")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#게임 화면 업데이트 속도
clock = pygame.time.Clock()

#assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

#배경 이미지 업로드
keyboard_image = pygame.image.load(os.path.join(assets_path, 'keyboard.png'))

keyboard_x = int(SCREEN_WIDTH/2)
keyboard_y = int(SCREEN_HEIGHT/2)
keyboard_dx = 0
keyboard_dy = 0

#게임 종료 전까지 반복
done = False

#게임반복구간
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #키가 눌릴 경우
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyboard_dx = -5
            elif event.key == pygame.K_RIGHT:
                keyboard_dx = 5
            elif event.key == pygame.K_UP:
                keyboard_dy = -5
            elif event.key == pygame.K_DOWN:
                keyboard_dx = -5
        #키가 놓일 경우
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                keyboard_dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                keyboard_dy = 0


    keyboard_x += keyboard_dx
    keyboard_y += keyboard_dy
    screen.fill(GRAY)
    screen.blit(keyboard_image, [keyboard_x, keyboard_y])
    pygame.display.flip()
    clock.tick(60)


#게임 종료
pygame.quit()
    

