import pygame
import os


#화면 크기
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 320

#색
LAND = (160, 120, 45)

#초기화
pygame.init()

#창이름
pygame.display.set_caption("이미지")

#스크린 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#게임 화면 업데이트 속도
clock = pygame.time.Clock()

#assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

#배경 이미지 업로드
background_image = pygame.image.load(os.path.join(assets_path, 'terrain.png'))

#버섯이미지 로드
mushroom_image_1 = pygame.image.load(os.path.join(assets_path, 'mushroom1.png'))
mushroom_image_2 = pygame.image.load(os.path.join(assets_path, 'mushroom2.png'))
mushroom_image_3 = pygame.image.load(os.path.join(assets_path, 'mushroom3.png'))

#게임 종료 전까지 반복
done = False

#게임반복구간
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #스크린 채우기
    screen.fill(LAND)

    #배경 이미지 그리기
    screen.blit(background_image, background_image.get_rect())

    #버섯 이미지 그리기
    screen.blit(mushroom_image_1, [100, 80])
    screen.blit(mushroom_image_2, [300, 100])
    screen.blit(mushroom_image_3, [450, 140])
    
    #초당 60프레임으로 화면 업데이트
    pygame.display.flip()

    clock.tick(60)

#게임 종료
pygame.quit()
