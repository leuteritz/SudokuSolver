
import pygame

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

WHITE = (200, 200, 200)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
clock = pygame.time.Clock()
running = True


def drawGrid():
    size = WINDOW_HEIGHT//9
    for i in range(0, WINDOW_WIDTH, size):
        for y in range(0, WINDOW_HEIGHT, size):
            pygame.draw.rect(screen, 'white', (i, y, size, size), 1)


while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    drawGrid()

    pygame.display.update()


pygame.quit()
