import pygame, time

black = (0, 0, 0)

def ending_game(display, score):
    clock = pygame.time.Clock()
    pivot = True
    x = 300
    sum = 5
    pivot1 = 1
    while pivot:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pivot = False
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_DOWN]:
                    return True
                else:
                    return False
        display.fill(black)

        if x > 600:
            pivot1 = 1
            sum = -1
        elif x > 580:
            if pivot1 == 1:
                sum = -2
            else:
                sum = 2
        elif x > 500:
            if pivot1 == 1:
                sum = -3
            else:
                sum = 3
        elif x > 400:
            if pivot1 == 1:
                sum = -5
            else:
                sum = 5
        elif x > 300:
            if pivot1 == 1:
                sum = -6
            else:
                sum = 6
        elif x > 200:
            if pivot1 == 1:
                sum = -5
            else:
                sum = 5
        elif x > 100:
            if pivot1 == 1:
                sum = -3
            else:
                sum = 3
        elif x > 20:
            if pivot1 == 1:
                sum = -2
            else:
                sum = 2
        elif x < 0:
            pivot1 = 0
            sum = 1
        x += sum

        pygame.draw.rect(display, (255, 255, 255), [x, 0, 100, 100], 3)
        pygame.draw.rect(display, (255, 255, 255), [600 - x, 600, 100, 100], 3)
        pygame.draw.rect(display, (255, 255, 255), [0, 600 - x, 100, 100], 3)
        pygame.draw.rect(display, (255, 255, 255), [600, x, 100, 100], 3)
        scorefont = pygame.font.SysFont("comicsansms", 50)
        label1 = scorefont.render("          Game Over!!", 1, (255, 255, 255))
        label2 = scorefont.render("          score : %d" % score, 1, (255, 255, 255))
        label3 = scorefont.render("   press down to restart", 1, (255, 255, 255))
        label4 = scorefont.render(" A+", 1, (255, 255, 255))
        label5 = scorefont.render(" C-", 1, (255, 255, 255))
        label6 = scorefont.render(" F", 1, (255, 255, 255))
        label7 = scorefont.render(" B0", 1, (255, 255, 255))
        display.blit(label1, (50, 200))
        display.blit(label2, (50, 300))
        display.blit(label3, (50, 400))
        display.blit(label4, (x, 10))
        display.blit(label5, (610 - x, 610))
        display.blit(label6, (20, 610 - x))
        display.blit(label7, (600, x + 10))



        pygame.display.flip
        pygame.display.update()

