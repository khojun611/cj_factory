import pygame
import sys
import random
from time import sleep
import time

padWidth = 480  # 게임화면의 가로크기
padHeight = 640  # 게임화면의 세로크기

rockImage = ['icecream.png', 'fried-chicken.png ', 'pizza.png ', 'cake.png ', 'hamburger.png ',
             'egg.png', 'broccoli.png', 'cabbage.png', 'carrot.png', 'vegetable.png',
             'cola.png', 'candies.png', 'chocolate.png', 'hotdog.png', 'salad.png',
             'fish.png', 'nuts.png', 'bananas.png', 'corn.png', 'glass-of-water.png']  # 음식 이미지 추가 - Yu 음식명에 따라 if문 and하기

# 메뉴에서 이미지 버튼 고르는 클래스 만들기ㅣ
# 플레이어1 플레이어2 클래스 나눠서 복붙
# 삭제해야되는 함수랑 변수 삭제
# 카운트 출력 이름바꾸기
# 게임오버시 출력 이미지
# 게임 클리어 조건 추가
# 게임 오버 조건 추가
# 음식 이름에 따라 if문 and 연산자로 만들기
# while true if shotcount 10이상 20이상 fightersize[0],[1] -- 나 ++ 하기 --
# 4 게임오버&클리어 화면 : 버튼 - 기존설정캐릭터로 유지하면서 다시시작,  나가기
# - 클리어 - 고백장면 나오고 그 장면 아래에 버튼 나오게
# - 게임오버 - 실패이미지(차이는) 나오고 그 장면 아래에 버튼 나오게

replaybuttonimg = pygame.image.load("replay.png")
exitbottonimg = pygame.image.load("exitimage")
gameDisplay = pygame.display.set_mode((padWidth, padHeight))
clock = pygame.time.Clock()




class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            gameDisplay.blit(img_in,(x,y))

class LoadBackground:
    def __init__(self, bg_img, bg_x, bg_y):
        self.bg_x = bg_x;
        self.bg_y = bg_y
        gameDisplay.blit(bg_img, (bg_x, bg_y))


def gameclear():
    clear = True

    while clear:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        clearbg = LoadBackground('clearimage.png', 0, 0)

        gameovertext = gameDisplay.blit('gameoverImg.png', (220, 150))
        replayButton = Button(replaybuttonimg, 280, 260, 60, 20, 'clickreStartImg.png', 273, 258, runGame())
        exitButton = Button(exitbottonimg, 445, 260, 60, 20, 'clickexitImg.png', 440, 258, quitgame())
        pygame.display.update()
        clock.tick(15)

def gameover():
    over = True

    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)
        clearbg = LoadBackground('clearimage.png', 0, 0)

        gameovertext = gameDisplay.blit('gameoverImg.png', (220, 150))
        replayButton = Button(replaybuttonimg, 280, 260, 60, 20, 'clickreStartImg.png', 273, 258, runGame())
        exitButton = Button(exitbottonimg, 445, 260, 60, 20, 'clickexitImg.png', 440, 258, quitgame())
        pygame.display.update()
        clock.tick(15)



explsionSound = ['eating1.wav', 'eating2.mp3', 'eating3.mp3']


# Sae 운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad
    # font = pygame.font.Font("폰트 경로인가?", 20)

    # % 기존 코드가 안되서 다른 방법을 찾아봄. 시스템에서 쓸수있는 폰트리스트를 뽑아서 그중 가장 대중적인 것으로 지정
    ableFonts = pygame.font.get_fonts()  # 폰트 리스트
    index = ableFonts.index("휴먼아미체")
    font = pygame.font.SysFont(str(ableFonts[index]), 30, True, True)
    text = font.render('파괴한 운석 수:' + str(count), True, (255, 255, 255))  # 감량, 증량 ,kg
    gamePad.blit(text, (10, 0))


# Sae 운석이 화면 아래로 통과한 개수- 삭제
def writePassed(count):
    global gamePad
    # font = pygame.font.Font("폰트", 20)

    # % 기존 코드가 안되서 다른 방법을 찾아봄. 시스템에서 쓸수있는 폰트리스트를 뽑아서 그중 가장 대중적인 것으로 지정
    ableFonts = pygame.font.get_fonts()  # 폰트 리스트
    index = ableFonts.index("휴먼아미체")
    font = pygame.font.SysFont(str(ableFonts[index]), 30, True, True)
    text = font.render('놓친 운석:' + str(count), True, (255, 0, 0))  # 삭제
    gamePad.blit(text, (360, 0))


# Han 게임 메세지 출력
def writeMessage(text):
    global gamePad
    # textfont = pygame.font.Font('폰트', 80)
    ableFonts = pygame.font.get_fonts()  # 폰트 리스트
    index = ableFonts.index("휴먼아미체")
    font = pygame.font.SysFont(str(ableFonts[index]), 30, True, True)
    text = font.render(text, True, (255, 0, 0))

    textpos = text.get_rect()
    textpos.center = (padWidth / 2, padHeight / 2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()
    gameOverSound.play()
    sleep(2)
    pygame.mixer.music.play(-1)
    runGame()


# Han 전투기가 운석과 충돌했을 때 메세지 출력 - 삭제
def crash():
    global gamePad
    writeMessage('전투기 파괴!')  # 삭제


# Han 게임 클리어, 오버

def gameclear():
    clear = True

    while clear:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)


        gameovertext = gameDisplay.blit(gameoverImg, (220, 150))
        restartButton = Button(restartImg, 280, 260, 60, 20, clickreStartImg, 273, 258, runGame())
        quitButton = Button(quitImg, 445, 260, 60, 20, clickQuitImg, 440, 258, quitgame)
        pygame.display.update()
        clock.tick(15)



# Han 게임에 등장하는 객체 드로잉
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))


def initGame():
    global gamePad, clock, background, fighter, missile, explosion, missileSound, gameOverSound
    pygame.init()  # Han
    gamePad = pygame.display.set_mode((padWidth, padHeight))  # Han

    pygame.display.set_caption('PyShooting')  # 게임 이름 추가 - Yu
    fighter = pygame.image.load('player.png')  # 전투기 그림 - ho #뚱뚱캐릭
    fighter2 = pygame.image.load('player2.png')  # 마른캐릭
    missile = pygame.image.load('spoon-and-fork.png')  # Sae 미사일그림
    explosion = pygame.image.load('mouth.png')  # 폭발 그림 - ho
    background = pygame.image.load('pig.png')  # Han
    clock = pygame.time.Clock()  # 시간 추척 추가 - Yu

    pygame.mixer.music.load('music.mp3')  # Chan 음악 재생
    pygame.mixer.music.play(-1)
    missileSound = pygame.mixer.Sound('throwing.mp3')
    gameOverSound = pygame.mixer.Sound('gameover.mp3')


def runGame():
    global gamepad, clock, background, fighter, missile, explosion, missileSound

    # 전투기 크기
    fighterSize = fighter.get_rect().size  # 할 수 있으면 늘리거나 줄이기
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    # 전투기 초기 위치 (x,y)
    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0
    fighterY = 0  # 플레이어 움직임 y값

    # Sae 무기좌표 리스트
    missileXY = []

    # 음식 랜덤 생성 - Yu
    rock = pygame.image.load(random.choice(rockImage))  # 파일 명인가?
    rockSize = rock.get_rect().size  # 운석 실제 크기
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    destroySound = pygame.mixer.Sound(random.choice(explsionSound))

    # 운석 초기 위치 설정 - Yu
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    rockSpeed = 2

    # 전투기 미사일에 운석이 맞았을 경우 True
    isShot = False
    shotCount = 0  # 여기
    rockPassed = 0

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:  # 게임 프로그램 종료
                pygame.quit()
                sys.exit()

            # 전투기 움직이기
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:  # 전투기 왼쪽으로 이동 참고
                    fighterX -= 5
                elif event.key == pygame.K_RIGHT:  # 전투기 오른쪽으로 이동
                    fighterX += 5
                elif event.key == pygame.K_UP:  # %플레이어가 위쪽으로 이동
                    fighterY -= 5
                elif event.key == pygame.K_DOWN:  # %플레이어가 아래쪽으로 이동
                    fighterY += 5
                elif event.key == pygame.K_SPACE:  # Sae 미사일발사
                    missileSound.play()
                    missileX = x + fighterWidth / 2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])

            if event.type in [pygame.KEYUP]:  # 방향키를 떼면
                # 플레이어가 멈춤
                # 위아래 움직임 추가
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    fighterX = 0
                    fighterY = 0

        drawObject(background, 0, 0)  # 배경화면 그리기 -Han
        drawObject(fighter, x, y)

        # 미사일 오브젝트 그리기
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        # Sae 미사일 발사 화면에 그리기
        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):  # Sae 미사일요소에 대해 반복함
                bxy[1] -= 10  # Sae 총알의 y좌표 -10 (위로 이동)
                missileXY[i][1] = bxy[1]

                if bxy[1] < rockY:
                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1  # + 5

                if bxy[1] <= 0:  # Sae 미사일이 화면 밖을 벗어나면
                    try:
                        missileXY.remove(bxy)  # Sae 미사일 제거
                    except:
                        pass

        # Sae 운석 맞춘 점수 표시
        writeScore(shotCount)

        rockY += rockSpeed  # 운석이 아래로 떨어질 때 y좌표 증가 - Yu
        # 운석이 지구로 떨어진 경우(화면 밖으로) - Yu
        if rockY > padHeight:
            # 새로운 운석 생성(랜덤)
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            rockPassed += 1

        if shotcount > 50:
            gameclear()

        elif shotcount < 0:
            gameover()



        # Sae 놓친 운석 수 표시
        writePassed(rockPassed)  # 삭제

        # 플레이어 위치 재조정
        x += fighterX
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth

        # 이게 게임패드 안에서만 움직이게 만드려고 하는 거 같은데
        y += fighterY
        if y < 0:
            y = 0
        elif y > padHeight - fighterHeight:
            y = padHeight - fighterHeight

        # Han 전투기가 운석과 충돌했는지 체크
        if y < rockY + rockHeight:
            if (rockX > x and rockX < x + fighterWidth) or (
                    rockX + rockWidth > x and rockX + rockWidth < x + fighterWidth):
                crash()

        # 운석을 맞춘 경우
        if isShot:

            # 운석 폭발
            drawObject(explosion, rockX, rockY)
            destroySound.play()

            # 새로운 운석(랜덤). 파괴되면 새로운 운석 생성
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            destroySound = pygame.mixer.Sound(random.choice(explsionSound))
            isShot = False

            # Han 운석 맞추면 속도 증가
            rockSpeed += 0.02
            if rockSpeed >= 10:
                rockSpeed = 10

        drawObject(rock, rockX, rockY)  # 장애물 그리기

        pygame.display.update()  # 게임화면을 다시 그림 -Han
        clock.tick(60)  # 게임화면의 초당 프레임수를 60으로 설정 - Yu

    pygame.quit()  # pygame 종료 - Yu


initGame()
runGame()
