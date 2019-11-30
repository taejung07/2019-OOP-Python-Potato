import pygame
import sys
import random
from pygame.locals import *
pygame.init()

WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)

BGCOLOR = WHITE
TEXTCOLOR = BLACK

BOARD_SIZE = 4

font = pygame.font.SysFont("monospace",25)

tileMatrix = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
undoMat = []

Font = pygame.font.Font('Typo_SsangmunDongB.ttf', 32)
screen = pygame.display.set_mode((480,320), DOUBLEBUF)
pygame.display.set_caption('2048 학점')

x_display = 425
y_display = 425

class Block:
    def __init__(self):
        self.image = pygame.image.load("D+.PNG")
        self.x = 0
        self.y = 0

    def move(self, background):
        key = pygame.key.get_pressed()
        dist = 50
        if key[pygame.K_DOWN]:
            self.y += dist
        elif key[pygame.K_UP]:
            self.y -= dist
        elif key[pygame.K_RIGHT]:
            self.x += dist
        elif key[pygame.K_LEFT]:
            self.x -= dist
        background.blit(self.image, (self.x, self.y))

def startdisplay():
    global x_display, y_display
    startscreen = pygame.display
    background = startscreen.set_mode((x_display, y_display))
    startscreen.set_caption('2048 학점')
    img = pygame.image.load("realbg.png")
    background.blit(img, (0,0))
    showtext('press space bar', x_display/2, y_display/2, BLACK)
    startscreen.update()

def playdisplay():
    playscreen = pygame.display
    background = playscreen.set_mode((x_display, y_display), DOUBLEBUF)
    img = pygame.image.load("realbg.png")
    background.blit(img, (0,0))
    playscreen.set_caption('2048 학점')
    showtext('두번째 화면!', x_display/2, y_display/2, BLACK)
    D_plus = Block()
    moving(D_plus, background)
    playscreen.update()

def moving(D_plus, background):
    #D_plus = Block()
    D_plus.move(background)

def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()

def showtext(text, x_pos, y_pos, color):
    titleSurf, titleRect = makeTextObjs(text, Font, color)
    titleRect.center = (x_pos, y_pos)
    screen.blit(titleSurf, titleRect)

rect = pygame.Rect((0,0), (32,32))
image = pygame.Surface((32,32))
image.fill(WHITE)


while True:
    startdisplay()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                while True:
                    playdisplay()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()