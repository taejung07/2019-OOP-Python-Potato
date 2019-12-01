#사용 방식 : ending_game 함수 호출 (display, score) 변수 사용

import pygame, time

vanilla = (255, 204, 154)

def ending_game(display, score):
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
                return event.type

        if x > 375:
            pivot1 = 1
            sum = -1
        elif x > 370:
            if pivot1 == 1:
                sum = -1.5
            else:
                sum = 1.5
        elif x > 320:
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
        pygame.draw.rect(display, (255, 204, 204), [370 - x, 370, 60, 60])
        pygame.draw.rect(display, (255, 255, 255), [370 - x, 370, 60, 60], 3)
        pygame.draw.rect(display, (255, 204, 204), [0, 370 - x, 60, 60])
        pygame.draw.rect(display, (255, 255, 255), [0, 370 - x, 60, 60], 3)
        pygame.draw.rect(display, (255, 204, 204), [370, x, 60, 60])
        pygame.draw.rect(display, (255, 255, 255), [370, x, 60, 60], 3)
        scorefont = pygame.font.SysFont("comicsansms", 32)
        scorefont2 = pygame.font.SysFont("comicsansms", 32)
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
        display.blit(label5, (370 - x, 370))
        display.blit(label6, (0, 370 - x))
        display.blit(label7, (370, x))

        pygame.display.flip
        pygame.display.update()

