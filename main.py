
import pygame

WINDOW_HEIGHT = 594
WINDOW_WIDTH = 594

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
clock = pygame.time.Clock()
running = True
number = ''

# font
font = pygame.font.Font(None, 36)


def drawGrid():
    size = WINDOW_HEIGHT//9
    for i in range(0, WINDOW_WIDTH, size):
        for j in range(0, WINDOW_HEIGHT, size):
            rect = pygame.Rect(i, j, size, size)

            pygame.draw.rect(screen, 'white', rect, 1, 10)
            number_text = font.render(number, True, 'white')
            screen.blit(
                number_text, (rect.x + (rect.w - number_text.get_width())/2, rect.y + (rect.h - number_text.get_height())/2))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isdigit():
                number += event.unicode

    screen.fill("black")
    drawGrid()

    pygame.display.flip()


pygame.quit()
