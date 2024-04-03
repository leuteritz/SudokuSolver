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

value = [['1', '4', '7', '5', '3', '6', '2', '9', '8'],
         ['2', '5', '8', '', '', '', '', '', ''],
         ['3', '6', '9', '', '', '', '', '', ''],
         ['4', '', '', '', '', '', '', '', ''],
         ['5', '', '', '', '', '', '', '', ''],
         ['6', '', '', '', '', '', '', '', ''],
         ['7', '', '', '', '', '', '', '', ''],
         ['8', '', '', '', '', '', '', '', ''],
         ['9', '', '', '', '', '', '', '', '']]


def rules(col, row, number):
    copy = [row[:] for row in value]
    copy[col][row] = number
    # Row
    for i in range(9):
        new_row = []
        count_dict = {str(i): 0 for i in range(1, 10)}
        test = 0
        for j in range(9):
            new_row.append(copy[j][i])

        for num in new_row:
            if num in count_dict:
                count_dict[num] += 1

        list_numer = list(count_dict.values())

        for i in range(len(count_dict)):
            if list_numer[i] == 1:
                test += 1

        if test != len([x for x in new_row if x != '']):
            return 1

    # Col
    for i in range(9):
        new_col = []
        count_dict = {str(i): 0 for i in range(1, 10)}
        test = 0
        for j in range(9):
            new_col.append(copy[i][j])

        for num in new_col:
            if num in count_dict:
                count_dict[num] += 1

        list_numer = list(count_dict.values())

        for i in range(len(count_dict)):
            if list_numer[i] == 1:
                test += 1

        if test != len([x for x in new_col if x != '']):
            return 1

    # Square
    for l in range(0, 7, 3):
        for i in range(0, 7, 3):

            new_square = []
            count_dict = {str(i): 0 for i in range(1, 10)}
            test = 0
            for j in range(3):

                for k in range(3):

                    new_square.append(copy[k + i][j + l])

            for num in new_square:
                if num in count_dict:
                    count_dict[num] += 1

            list_numer = list(count_dict.values())

            for i in range(len(count_dict)):
                if list_numer[i] == 1:
                    test += 1

            if test != len([x for x in new_square if x != '']):
                return 1

    return 0


wrong = None


def drawGrid():
    a = 0
    b = 0
    for i in range(0, WINDOW_WIDTH, SIZE):
        b = 0
        for j in range(0, WINDOW_HEIGHT, SIZE):
            rect = pygame.Rect(i, j, SIZE, SIZE)

            pygame.draw.rect(screen, 'gray', rect, 2)

            # draw number inside cell
            number_text = font.render(value[a][b], True, 'black')
            screen.blit(
                number_text, (rect.x + (rect.w - number_text.get_width())/2, rect.y + (rect.h - number_text.get_height())/2))

            # draw game corner border
            if a == 3 or a == 6:
                pygame.draw.rect(screen, 'black', (i - 5, j, 10, SIZE))
            if b == 3 or b == 6:
                pygame.draw.rect(screen, 'black', (i, j - 5, SIZE, 10))

            # draw a green border in selected cell
            if selected_cell is not None and selected_cell == (b, a):
                if (wrong == True):
                    pygame.draw.rect(screen, 'red', rect, 5)
                else:
                    pygame.draw.rect(screen, 'green', rect, 5)

            b += 1

        a += 1


def updateGrid(row, col, number):
    global wrong
    if rules(col, row, number) == 0:
        print(f"New Number {number} at [{col}][{row}]")
        value[col][row] = number
        wrong = False
    else:

        wrong = True


selected_cell = None


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            clicked_row = mouse_pos[1] // SIZE
            clicked_col = mouse_pos[0] // SIZE
            selected_cell = (clicked_row, clicked_col)
            wrong = False

        elif event.type == pygame.KEYDOWN:
            if pygame.K_1 <= event.key <= pygame.K_9:
                number = chr(event.key)
                updateGrid(clicked_row, clicked_col, number)

    screen.fill("white")
    drawGrid()

    pygame.display.flip()

pygame.quit()
