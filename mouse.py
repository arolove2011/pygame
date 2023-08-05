import pygame
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)

pygame.init()

pygame.display.set_caption("마우스")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#게임 화면 업데이트 속도
clock = pygame.time.Clock()

#assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

#마우스 이미지 업로드
mouse_image = pygame.image.load(os.path.join(assets_path, 'mouse.png'))

mouse_x = int(SCREEN_WIDTH/2)
mouse_y = int(SCREEN_HEIGHT/2)

#마우스 커서 숨기기
pygame.mouse.set_visible(False)

#게임 종료 전까지 반복
done = False

#게임반복구간
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #마우스 위치 값 가져오기
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]

    #마우스 이미지 그리기
    screen.fill(WHITE)
    screen.blit(mouse_image, [mouse_x, mouse_y])
    pygame.display.flip()
    clock.tick(60)


#게임 종료
pygame.quit()