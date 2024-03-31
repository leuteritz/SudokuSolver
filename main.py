import pygame

WINDOW_HEIGHT = 594
WINDOW_WIDTH = 594
SIZE = WINDOW_HEIGHT//9

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
pygame.display.set_caption("Sudoku")

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

            pygame.draw.rect(screen, 'gray', rect, 2)
            number_text = font.render(list[a][b], True, 'black')
            screen.blit(
                number_text, (rect.x + (rect.w - number_text.get_width())/2, rect.y + (rect.h - number_text.get_height())/2))

            # draw game corner border
            if a == 3 or a == 6:
                pygame.draw.rect(screen, 'black', (i - 5, j, 10, SIZE))
            if b == 3 or b == 6:
                pygame.draw.rect(screen, 'black', (i, j - 5, SIZE, 10))

            # draw a green border in selected cell
            if selected_cell is not None and selected_cell == (b, a):

                pygame.draw.rect(screen, 'green', rect, 5)

            b += 1

        a += 1


def updateGrid(row, col, number):
    list[col][row] = number


selected_cell = None


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            clicked_row = mouse_pos[1] // SIZE
            clicked_col = mouse_pos[0] // SIZE
            selected_cell = (clicked_row, clicked_col)

        elif event.type == pygame.KEYDOWN:

            if pygame.K_1 <= event.key <= pygame.K_9:
                number = chr(event.key)
                updateGrid(clicked_row, clicked_col, number)

    screen.fill("white")
    drawGrid()

    pygame.display.flip()


pygame.quit()
