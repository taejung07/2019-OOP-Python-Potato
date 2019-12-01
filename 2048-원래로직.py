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
scorefont = pygame.font.SysFont("comicsans", 40)

tileMatrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
undoMat = []


def main(fromLoaded = False):
    if not fromLoaded:
        placeRandomTile()
        placeRandomTile()

    printMatrix()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if checkIfCanGo() == True:
                if event.type == KEYDOWN:
                    if isArrow(event.key):
                        rotations = getRotations(event.key)

                        addToUndo()

                        for i in range(0, rotations):
                            rotateMatrixClockwise()

                        if canMove():
                            moveTiles()
                            mergeTiles()
                            placeRandomTile()

                        for j in range(0, (4 - rotations) % 4):
                            rotateMatrixClockwise()

                        printMatrix()
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


def moveTiles():
    for i in range(0, 4):
        for j in range(0, 4 - 1):
            while tileMatrix[i][j] == 0 and sum(tileMatrix[i][j:]) > 0:
                for k in range(j, 4 - 1): 
                    tileMatrix[i][k] = tileMatrix[i][k + 1]
                tileMatrix[i][4 - 1] = 0


def mergeTiles():
    global TOTAL_POINTS
    
    for i in range(0, 4):
        for k in range(0, 4 - 1):
                if tileMatrix[i][k] == tileMatrix[i][k + 1] and tileMatrix[i][k] != 0:
                    tileMatrix[i][k] = tileMatrix[i][k] * 2
                    tileMatrix[i][k + 1] = 0
                    moveTiles()
                
def canMove():
    for i in range(0, 4):
        for j in range(1, 4):
            if tileMatrix[i][j-1] == 0 and tileMatrix[i][j] > 0:
                return True
            elif (tileMatrix[i][j-1] == tileMatrix[i][j]) and tileMatrix[i][j-1] != 0:
                return True

    return False

def getRotations(k):
    if k == pygame.K_UP:
        return 0
    elif k == pygame.K_DOWN:
        return 2
    elif k == pygame.K_LEFT:
        return 1
    elif k == pygame.K_RIGHT:
        return 3


def rotateMatrixClockwise():
    for i in range(0, int(4/2)):
        for k in range(i, 4- i - 1):
            temp1 = tileMatrix[i][k]
            temp2 = tileMatrix[4 - 1 - k][i]
            temp3 = tileMatrix[4 - 1 - i][4 - 1 - k]
            temp4 = tileMatrix[k][4 - 1 - i]
    
            tileMatrix[4 - 1 - k][i] = temp1
            tileMatrix[4 - 1 - i][4 - 1 - k] = temp2
            tileMatrix[k][4 - 1 - i] = temp3
            tileMatrix[i][k] = temp4


def printMatrix():
    SURFACE.fill((240, 240, 206))
    board = pygame.Rect(50, 50, 400, 400)
    color = (186, 173, 160)
    pygame.draw.rect(SURFACE, color, board)

    global Score

    max = 2
    for i in range(0, 4):
        for j in range(0, 4):
            if tileMatrix[i][j] == 2:
                block = D_plus()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
            elif tileMatrix[i][j] == 4:
                block = C_minus()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 4:
                    max = 4
                    Score = "C-"
            elif tileMatrix[i][j] == 8:
                block = C_zero()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 8:
                    max = 8
                    Score = "C0"
            elif tileMatrix[i][j] == 16:
                block = C_plus()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 16:
                    max = 16
                    Score = "C+"
            elif tileMatrix[i][j] == 32:
                block = B_minus()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 32:
                    max = 32
                    Score = "B-"
            elif tileMatrix[i][j] == 64:
                block = B_zero()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 64:
                    max = 64
                    Score = "B0"
            elif tileMatrix[i][j] == 128:
                block = B_plus()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 128:
                    max = 128
                    Score = "B+"
            elif tileMatrix[i][j] == 256:
                block = A_minus()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 256:
                    max = 256
                    Score = "A-"
            elif tileMatrix[i][j] == 512:
                block = A_zero()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 512:
                    max = 512
                    Score = "A0"
            elif tileMatrix[i][j] == 1024:
                block = A_plus()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()
                if max < 1024:
                    max = 1024
                    Score = "A+"
            else:
                pygame.draw.rect(SURFACE, (120,110,101), (60 + i * 87 + 10 * i, 60 + j * 87 + 10 * j, 87, 87))

            pygame.draw.rect(SURFACE, (240, 240, 206), (8, 8, 130, 30))
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


def placeRandomTile():
    count = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if tileMatrix[i][j] == 0:
                count += 1
    
    k = floor(random() * 4 * 4)
    
    while tileMatrix[floor(k / 4)][k % 4] != 0:
        k = floor(random() * 4 * 4)
    
    tileMatrix[floor(k / 4)][k % 4] = 2


def floor(n):
    return int(n - (n % 1))



def checkIfCanGo():
    for i in range(0, 4 ** 2):
        if tileMatrix[floor(i / 4)][i % 4] == 0:
            return True

    for i in range(0, 4):
        for j in range(0, 4 - 1):
            if tileMatrix[i][j] == tileMatrix[i][j + 1]:
                return True
            elif tileMatrix[j][i] == tileMatrix[j + 1][i]:
                return True
    return False


def reset():
    global Score
    global tileMatrix

    Score = "D+"
    SURFACE.fill(BLACK)

    tileMatrix = [[0 for i in range(0, 4)] for j in range(0, 4)]

    main()


def isArrow(k):
    return (k == pygame.K_UP or k == pygame.K_DOWN or k == pygame.K_LEFT or k == pygame.K_RIGHT)


def saveGameState():
    f = open("savedata", "w")

    line1 = " ".join([str(tileMatrix[floor(x / 4)][x % 4]) for x in range(0, 4 ** 2)])

    f.write(line1 + "\n")
    f.write(str(4) + "\n")
    f.write(str(Score))
    f.close()


def loadGameState():
    global Score
    global tileMatrix

    f = open("savedata", "r")

    mat = (f.readline()).split(' ', 4 ** 2)
    Score = int(f.readline())

    for i in range(0, 4 ** 2):
        tileMatrix[floor(i / 4)][i % 4] = int(mat[i])

    f.close()

    main(True)


def convertToLinearground():
    mat = []

    for i in range(0, 4 ** 2):
        mat.append(tileMatrix[floor(i / 4)][i % 4])

    mat.append(Score)

    return mat


def addToUndo():
    undoMat.append(convertToLinearground())


def undo():
    if len(undoMat) > 0:
        mat = undoMat.pop()

        for i in range(0, 4 ** 2):
            tileMatrix[floor(i / 4)][i % 4] = mat[i]

        global Score
        Score = mat[4 ** 2]

        printground()


main()