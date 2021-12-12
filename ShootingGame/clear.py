import pygame
import sys
import random
from time import sleep
import time


replaybotton = pygame.image.load("replay.png")
exitbotton = pygame.image.load("exitimage")
gameDisplay = pygame.display.set_mode((display_width, display_height))
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

        gameovertext = gameDisplay.blit(gameoverImg, (220, 150))
        restartButton = Button(restartImg, 280, 260, 60, 20, clickreStartImg, 273, 258, runGame())
        quitButton = Button(quitImg, 445, 260, 60, 20, clickQuitImg, 440, 258, quitgame)
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


        gameovertext = gameDisplay.blit(gameoverImg, (220, 150))
        restartButton = Button(replaybottonImg, 280, 260, 60, 20, clickreStartImg, 273, 258, runGame())
        quitButton = Button(exitbottonImg, 445, 260, 60, 20, clickQuitImg, 440, 258, quitgame)
        pygame.display.update()
        clock.tick(15)

#--------------------------------------runGame()안에 넣기------------------------------------------------------------

if shotcount > 50:
    gameclear()

elif shotcount < 0:
    gameover()




