import pygame

WINDOW_HEIGHT = 594
WINDOW_WIDTH = 594
SIZE = WINDOW_HEIGHT//9

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
clock = pygame.time.Clock()
running = True
number = ''

# font
font = pygame.font.Font(None, 36)

list = [['1', '9', '3', '1', '2', '3', '1', '2', '3'],
        ['2', '8', '3', '1', '2', '3', '1', '2', '3'],
        ['3', '7', '3', '1', '2', '3', '1', '2', '3'],
        ['4', '6', '3', '1', '2', '3', '1', '2', '3'],
        ['5', '5', '3', '1', '2', '3', '1', '2', '3'],
        ['6', '4', '3', '1', '2', '3', '1', '2', '3'],
        ['7', '3', '3', '1', '2', '3', '1', '2', '3'],
        ['8', '2', '3', '1', '2', '3', '1', '2', '3'],
        ['9', '1', '3', '1', '2', '3', '1', '2', '3']]


def drawGrid():
    a = 0
    b = 0
    for i in range(0, WINDOW_WIDTH, SIZE):
        b = 0  # Reset column index for each row
        for j in range(0, WINDOW_HEIGHT, SIZE):
            rect = pygame.Rect(i, j, SIZE, SIZE)

            pygame.draw.rect(screen, 'white', rect, 1, 10)
            number_text = font.render(list[a][b], True, 'white')
            screen.blit(
                number_text, (rect.x + (rect.w - number_text.get_width())/2, rect.y + (rect.h - number_text.get_height())/2))
            b += 1

        a += 1


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            clicked_row = mouse_pos[1] // SIZE
            clicked_col = mouse_pos[0] // SIZE
            list[clicked_col][clicked_row] = '4'

    screen.fill("black")
    drawGrid()

    pygame.display.flip()


pygame.quit()
