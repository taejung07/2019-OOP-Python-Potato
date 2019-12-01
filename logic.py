import random
import pygame

background = [[-1]*4 for i in range(4)]

class Block:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self):
        screen.blit(self.image, (self.x, self.y))

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
    random_x1 = random.randint(0, 3)
    random_y1 = random.randint(0, 3)
    if background[random_x1][random_y1] == -1:
        background[random_x1][random_y1] = 0
    else:
        new_block()


def combine_block():
    global background
    key = pygame.key.get_pressed()
    blank = []
    if key[pygame.K_UP]:
        for i in range(0, 4):
            for j in range(3, -1, -1):
                for k in range(j-1, -1, -1):
                    if background[j][i] == background[k][i]:
                        background[k][i] +=1
                        background[j][i] = -1
        for i in range(0, 4):
            for j in range(0, 4):
                if background[j][i] != -1:
                    blank.append(j)
            for k in range(len(blank)):
                background[k][i] = background[blank[k]][i]
            for k in range(len(blank)+1, 4):
                background[k][i] = -1

    elif key[pygame.K_DOWN]:
        flag = 0
        for i in range(0, 4):
            for j in range(0, 4):
                for k in range(j+1, 4):
                    if background[j][i] == background[k][i]:
                        background[k][i] += 1
                        background[j][i] = -1
        for i in range(0, 4):
            for j in range(3, -1, -1):
                if background[j][i] != -1:
                    blank.append(j)
            for k in range(3, 3-len(blank), -1):
                background[k][i] = background[blank[flag]][i]
                flag += 1
            for k in range(3-len(blank), -1, -1):
                background[k][i] = -1

    elif key[pygame.K_RIGHT]:
        flag = 0
        for i in range(0, 4):
            for j in range(0, 4):
                for k in range(j+1, 4):
                    if background[i][j] == background[i][k]:
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

    elif key[pygame.K_LEFT]:
        for i in range(0, 4):
            for j in range(3, -1, -1):
                for k in range(j-1, -1, -1):
                    if background[i][j] == background[i][k]:
                        background[i][k] += 1
                        background[i][j] = -1
        for i in range(0, 4):
            for j in range(0, 4):
                if background[i][j] != -1:
                    blank.append(j)
            for k in range(0, len(blank)+1):
                background[i][k] = background[i][blank[k]]
            for k in range(len(blank)+1, 4):
                background[i][k] = -1