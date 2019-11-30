import pygame

pygame.init()

class Bird(object):  # represents the bird, not the game
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load("D+.PNG")
        # the bird's position
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = 0
        self.y = 0

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 50 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))

screen = pygame.display.set_mode((640, 400))

bird = Bird() # create an instance
clock = pygame.time.Clock()

def move(bird, start_x, start_y, end_x, end_y, screen):
    for i in range(start_x, end_x):
        bird.x = i
        clock.tick(120)
        bird.draw(screen)
        pygame.display.update()
        pygame.display.flip()

    for j in range(start_y, end_y):
        bird.y = j
        clock.tick(120)
        bird.draw(screen)
        pygame.display.update()
        pygame.display.flip()


running = True
while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False

    bird.handle_keys() # handle the keys

    screen.fill((255,255,255)) # fill the screen with white
    bird.draw(screen) # draw the bird to the screen
    pygame.display.update() # update the screen

    move(bird, 0, 0, 100, 100, screen)

    clock.tick(40)
