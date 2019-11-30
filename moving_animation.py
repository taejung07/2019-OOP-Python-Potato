#사용법
#def moving(display, 처음 x 좌표, 처음 y 좌표, 나중 x 좌표, 나중 y 좌표, imagefile(png 형태로)):
import pygame

def moving(display, sx, sy, ex, ey, imagefile):
    x = sx
    y = sy
    bx = x
    by = y
    size = 100
    clock = pygame.time.Clock()

    while True:
        clock.tick(120)
        img = pygame.image.load("realbg.png")
        if bx == x:
                display.blit(img, (bx, by), pygame.Rect(sx, by, size, size))
        elif by == y:
            display.blit(img, (bx, by), pygame.Rect(bx, sy, size, size))
        img = pygame.image.load(imagefile)
        image = pygame.transform.scale(img, (size, size))
        display.blit(image, (x, y))

        if ex == sx:
            if sy > ey:
                by = y
                y -= 3
            else:
                by = y
                y += 3
        else:
            if sx > ex:
                bx = x
                x -= 3
            else:
                bx = x
                x += 3
        if x <= ex + 3 and x >= ex-3 and y <= ey + 3 and y >= ey-3:
            break

        pygame.display.flip
        pygame.display.update()