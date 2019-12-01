import pygame, sys, time
from pygame.locals import *
from random import *


Score = "D+"

pygame.init()

SURFACE = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("2048")

scorefont = pygame.font.SysFont("comicsans", 40)

background = [[-1]*4 for i in range(4)]


def main(fromLoaded = False):
    if not fromLoaded:
        new_block()
        new_block()

    printground()
    event_type = ''
    event_key = ''
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if checkIfCanGo() == True:
                if event.type == KEYDOWN:
                    if canMove():
                        combine_block(event.key)

                        new_block()
                        new_block()
                    printground()
            else:
                event_type, event_key = printGameOver(SURFACE)

            if event_type == KEYDOWN:

                if event_key == pygame.K_r:
                    reset()


        pygame.display.update()


class Block:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self):
        SURFACE.blit(pygame.transform.scale(self.image, (87, 87)), (self.x, self.y))

class Blank(Block):
    def __init__(self):
        self.image = pygame.image.load("Blank.PNG")

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
        background[random_x1][random_y1] = 0
    else:
        new_block()


def canMove():
    for i in range(0, 4):
        for j in range(1, 4):
            if background[i][j-1] == -1 and background[i][j] > -1:
                return True
            elif (background[i][j-1] == background[i][j]) and background[i][j-1] != -1:
                return True

    return False


def combine_block(key):
    global background

    blank = []
    if key == pygame.K_LEFT:
        for i in range(0, 4):
            for j in range(3, -1, -1):
                for k in range(j-1, -1, -1):
                    if background[j][i] == background[k][i] and background[j][i] != -1:
                        background[k][i] += 1
                        background[j][i] = -1
        for i in range(0, 4):
            for j in range(0, 4):
                if background[j][i] != -1:
                    blank.append(j)
            for k in range(len(blank)):
                background[k][i] = background[blank[k]][i]
            for k in range(len(blank) + 1, 4):
                background[k][i] = -1

    elif key == pygame.K_DOWN:
        flag = 0
        for i in range(0, 4):
            for j in range(0, 4):
                for k in range(j+1, 4):
                    if background[j][i] == background[k][i] and background[j][i] != -1:
                        background[k][i] += 1
                        background[j][i] = -1
        for i in range(0, 4):
            for j in range(3, -1, -1):
                if background[j][i] != -1:
                    blank.append(j)
            for k in range(3, 2-len(blank), -1):
                background[k][i] = background[blank[flag]][i]
                flag += 1
            for k in range(2-len(blank), -1, -1):
                background[k][i] = -1

    elif key == pygame.K_RIGHT:
        flag = 0
        for i in range(0, 4):
            for j in range(0, 4):
                for k in range(j+1, 4):
                    if background[i][j] == background[i][k] and background[i][j] != -1:
                        background[i][k] += 1
                        background[i][j] = -1
        for i in range(0, 4):
            for j in range(3, -1, -1):
                if background[i][j] != -1:
                    blank.append(j)
            for k in range(3, 3-len(blank), -1):
                background[i][k] = background[i][blank[flag]]
                flag += 1
            for k in (3-len(blank), -1, -1):
                background[i][k] = -1

    elif key == pygame.K_UP:
        for i in range(0, 4):
            for j in range(3, -1, -1):
                for k in range(j-1, -1, -1):
                    if background[i][j] == background[i][k] and background[i][j] != -1:
                        background[i][k] += 1
                        background[i][j] = -1
        for i in range(0, 4):
            for j in range(0, 4):
                if background[i][j] != -1:
                    blank.append(j)
            for k in range(0, len(blank) + 1):
                background[i][k] = background[i][blank[k]]
            for k in range(len(blank) + 1, 4):
                background[i][k] = -1


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
                block = Blank()
                block.x = 60 + i * 87 + 10 * i
                block.y = 60 + j * 87 + 10 * j
                block.move()

            pygame.draw.rect(SURFACE, (240, 240, 206), (8, 8, 150, 30))
            label = scorefont.render("Grade:" + " " + Score, 1, (0, 0, 0))

            SURFACE.blit(label, (10, 10))


def printGameOver(display):
    global Score
    score = Score
    clock = pygame.time.Clock()
    pivot = True
    x = 300
    sum = 5
    pivot1 = 1

    while pivot:
        img = pygame.image.load("realbg.png")
        display.blit(img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                return event.type, event.key

        if x > 450:
            pivot1 = 1
            sum = -1
        elif x > 400:
            if pivot1 == 1:
                sum = -1.5
            else:
                sum = 1.5
        elif x > 350:
            if pivot1 == 1:
                sum = -2.5
            else:
                sum = 2.5
        elif x > 300:
            if pivot1 == 1:
                sum = -4
            else:
                sum = 4
        elif x > 250:
            if pivot1 == 1:
                sum = -5
            else:
                sum = 5
        elif x > 150:
            if pivot1 == 1:
                sum = -4
            else:
                sum = 4
        elif x > 75:
            if pivot1 == 1:
                sum = -2.5
            else:
                sum = 2.5
        elif x > 25:
            if pivot1 == 1:
                sum = -1.5
            else:
                sum = 1.5
        elif x < 0:
            pivot1 = 0
            sum = 1
        x += sum

        pygame.draw.rect(display, (255, 204, 204), [x, 0, 60, 60])
        pygame.draw.rect(display, (255, 255, 255), [x, 0, 60, 60], 3)
        pygame.draw.rect(display, (255, 204, 204), [430 - x, 370, 60, 60])
        pygame.draw.rect(display, (255, 255, 255), [430 - x, 370, 60, 60], 3)
        pygame.draw.rect(display, (255, 204, 204), [0, 430 - x, 60, 60])
        pygame.draw.rect(display, (255, 255, 255), [0, 430 - x, 60, 60], 3)
        pygame.draw.rect(display, (255, 204, 204), [430, x, 60, 60])
        pygame.draw.rect(display, (255, 255, 255), [430, x, 60, 60], 3)
        scorefont = pygame.font.SysFont("comicsansms", 35)
        scorefont2 = pygame.font.SysFont("comicsansms", 35)
        label1 = scorefont2.render("Game Over!!", 1, (102, 51, 51))
        label2 = scorefont2.render("score : %d" % score, 1, (102, 51, 51))
        label3 = scorefont2.render("press any key to restart!", 1, (102, 51, 51))
        pygame.draw.polygon(display, (255, 255, 255), [[275, 420], [325, 420], [300, 460]])
        label4 = scorefont.render(" A+", 1, (255, 255, 255))
        label5 = scorefont.render(" C-", 1, (255, 255, 255))
        label6 = scorefont.render(" D", 1, (255, 255, 255))
        label7 = scorefont.render(" B0", 1, (255, 255, 255))
        display.blit(label1, (130, 100))
        display.blit(label2, (130, 180))
        display.blit(label3, (35, 260))
        display.blit(label4, (x, 0))
        display.blit(label5, (430 - x, 4300))
        display.blit(label6, (0, 430 - x))
        display.blit(label7, (430, x))

        pygame.display.flip
        pygame.display.update()


def floor(n):
    return int(n - (n % 1))


def checkIfCanGo():
    for i in range(0, 4 ** 2):
        if background[floor(i / 4)][i % 4] == -1:
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


main()