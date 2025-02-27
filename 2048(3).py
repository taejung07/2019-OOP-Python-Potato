# 2048 Game written using the Pygame module
# 
# Lewis Deane
# 23/12/2014

import pygame, sys, time
from pygame.locals import *
from colours import *
from random import *


Score = "D+"
DEFAULT_SCORE = 2

pygame.init()

SURFACE = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("2048")

myfont = pygame.font.SysFont("comicsans", 30)
scorefont = pygame.font.SysFont("comicsans", 50)

background = [[-1]*4 for i in range(4)]
undoMat = []


def main(fromLoaded = False):
    if not fromLoaded:
        new_block()
        new_block()

    printground()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if checkIfCanGo() == True:
                if event.type == KEYDOWN:
                    combine_block(event.key)

                    new_block()
                    new_block()
                    printground()
            else:
                printGameOver()

            if event.type == KEYDOWN:

                if event.key == pygame.K_r:
                    reset()

                if event.key == pygame.K_s:
                    saveGameState()
                elif event.key == pygame.K_l:
                    loadGameState()
                elif event.key == pygame.K_u:
                    undo()

        pygame.display.update()


class Block:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self):
        SURFACE.blit(pygame.transform.scale(self.image, (87, 87)), (self.x, self.y))

class D_plus(Block):
    def __init__(self):
        self.image = pygame.image.load("D+.PNG")

class C_plus(Block):
    def __init__(self):
        self.image = pygame.image.load("C+.PNG")

class C_zero(Block):
    def __init__(self):
        self.image = pygame.image.load("C0.PNG")

class C_minus(Block):
    def __init__(self):
        self.image = pygame.image.load("C-.PNG")

class B_plus(Block):
    def __init__(self):
        self.image = pygame.image.load("B+.PNG")

class B_zero(Block):
    def __init__(self):
        self.image = pygame.image.load("B0.PNG")

class B_minus(Block):
    def __init__(self):
        self.image = pygame.image.load("B-.PNG")

class A_plus(Block):
    def __init__(self):
        self.image = pygame.image.load("A+.PNG")

class A_zero(Block):
    def __init__(self):
        self.image = pygame.image.load("A0.PNG")

class A_minus(Block):
    def __init__(self):
        self.image = pygame.image.load("A-.PNG")

def new_block(): #두 번씩 실행해야 함.
    global background

    random_x1 = randint(0, 3)
    random_y1 = randint(0, 3)
    if background[random_x1][random_y1] == -1:
        print(random_x1, random_y1)
        background[random_x1][random_y1] = 0


def combine_block(key):
    global background

    blank = []
    logic = []
    if key == pygame.K_UP:
        for i in range(0, 4):
            for j in range(0, 4):
                logic.append(background[i][j])

            while -1 in logic:
                del logic[logic.index(-1)]

            for j in range(0, len(logic)-1):
                if logic[j] == logic[j+1]:
                    logic[j] += 1
                    logic[j+1] = -1

            while -1 in logic:
                del logic[logic.index(-1)]

            for j in range(0, len(logic)):
                background[i][j] = logic[j]
            for j in range(len(logic), 4):
                background[i][j] = -1

            logic = []

    elif key == pygame.K_RIGHT:
        flag = 0
        for i in range(0, 4):
            for j in range(3, -1, -1):
                logic.append(background[j][i])

            while -1 in logic:
                del logic[logic.index(-1)]

            for j in range(0, len(logic)-1):
                if logic[j] == logic[j+1]:
                    logic[j] += 1
                    logic[j+1] = -1

            while -1 in logic:
                del logic[logic.index(-1)]

            for j in range(3, 3-len(logic), -1):
                background[j][i] = logic[flag]
                flag += 1
            for j in range(3-len(logic), -1, -1):
                background[j][i] = -1
            flag = 0

            logic = []

    elif key == pygame.K_DOWN:
        flag = 0
        for i in range(0, 4):
            for j in range(3, -1, -1):
                logic.append(background[i][j])

            while -1 in logic:
                del logic[logic.index(-1)]

            for j in range(0, len(logic)-1):
                if logic[j] == logic[j+1]:
                    logic[j] += 1
                    logic[j+1] = -1

            while -1 in logic:
                del logic[logic.index(-1)]

            for j in range(3, 3-len(logic), -1):
                background[i][j] = logic[flag]
                flag += 1
            for j in range(3-len(logic), -1, -1):
                background[i][j] = -1
            flag = 0

            logic = []

    elif key == pygame.K_LEFT:
        for i in range(0, 4):
            for j in range(0, 4):
                logic.append(background[j][i])

            while -1 in logic:
                del logic[logic.index(-1)]

            for j in range(0, len(logic)-1):
                if logic[j] == logic[j+1]:
                    logic[j] += 1
                    logic[j+1] = -1

            while -1 in logic:
                del logic[logic.index(-1)]

            print(len(logic))

            for j in range(0, len(logic)):
                background[j][i] = logic[j]
            for j in range(len(logic), 4):
                background[j][i] = -1
            logic = []


def printground():
    SURFACE.fill((240, 240, 206))
    board = pygame.Rect(50, 50, 400, 400)
    color = (186, 173, 160)
    pygame.draw.rect(SURFACE, color, board)

    global Score

    max = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if background[i][j] == 0:
                block = D_plus()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
            elif background[i][j] == 1:
                block = C_minus()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 1:
                    max = 1
                    Score = "C-"
            elif background[i][j] == 2:
                block = C_zero()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 2:
                    max = 2
                    Score = "C0"
            elif background[i][j] == 3:
                block = C_plus()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 3:
                    max = 3
                    Score = "C+"
            elif background[i][j] == 4:
                block = B_minus()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 4:
                    max = 4
                    Score = "B-"
            elif background[i][j] == 5:
                block = B_zero()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 5:
                    max = 5
                    Score = "B0"
            elif background[i][j] == 6:
                block = B_plus()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 6:
                    max = 6
                    Score = "B+"
            elif background[i][j] == 7:
                block = A_minus()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 7:
                    max = 7
                    Score = "A-"
            elif background[i][j] == 8:
                block = A_zero()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 8:
                    max = 8
                    Score = "A0"
            elif background[i][j] == 9:
                block = A_plus()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 9:
                    max = 9
                    Score = "A+"
            else:
                pygame.draw.rect(SURFACE, (120,110,101), (60 + i * 87 + 10 * i, 60 + j * 87 + 10 * j, 87, 87))

            label = scorefont.render("Grade:" + Score, 1, BLACK)

            SURFACE.blit(label, (10, 10))


def printGameOver():
    global Score

    SURFACE.fill(BLACK)

    label = scorefont.render("Semester is finished", 1, (255, 255, 255))
    label2 = scorefont.render("Final Grade:" + Score, 1, (255, 255, 255))
    label3 = myfont.render("press r to restart!", 1, (255, 255, 255))

    SURFACE.blit(label, (50, 100))
    SURFACE.blit(label2, (50, 200))
    SURFACE.blit(label3, (50, 300))



def floor(n):
    return int(n - (n % 1))



def checkIfCanGo():
    for i in range(0, 4 ** 2):
        if background[floor(i / 4)][i % 4] == 0:
            return True

    for i in range(0, 4):
        for j in range(0, 4 - 1):
            if background[i][j] == background[i][j + 1]:
                return True
            elif background[j][i] == background[j + 1][i]:
                return True
    return False


def reset():
    global Score
    global background

    Score = "D+"
    SURFACE.fill(BLACK)

    background = [[0 for i in range(0, 4)] for j in range(0, 4)]

    main()


def isArrow(k):
    return (k == pygame.K_UP or k == pygame.K_DOWN or k == pygame.K_LEFT or k == pygame.K_RIGHT)


def saveGameState():
    f = open("savedata", "w")

    line1 = " ".join([str(background[floor(x / 4)][x % 4]) for x in range(0, 4 ** 2)])

    f.write(line1 + "\n")
    f.write(str(4) + "\n")
    f.write(str(Score))
    f.close()


def loadGameState():
    global Score
    global background

    f = open("savedata", "r")

    mat = (f.readline()).split(' ', 4 ** 2)
    Score = int(f.readline())

    for i in range(0, 4 ** 2):
        background[floor(i / 4)][i % 4] = int(mat[i])

    f.close()

    main(True)


def convertToLinearground():
    mat = []

    for i in range(0, 4 ** 2):
        mat.append(background[floor(i / 4)][i % 4])

    mat.append(Score)

    return mat


def addToUndo():
    undoMat.append(convertToLinearground())


def undo():
    if len(undoMat) > 0:
        mat = undoMat.pop()

        for i in range(0, 4 ** 2):
            background[floor(i / 4)][i % 4] = mat[i]

        global Score
        Score = mat[4 ** 2]

        printground()


main()