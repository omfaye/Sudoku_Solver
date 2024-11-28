import pygame
import time

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 540, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)
FONT = pygame.font.Font(None, 40)

# Setup the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Sample Sudoku puzzle
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def draw_grid():
    WIN.fill(WHITE)
    # Draw the grid lines
    for i in range(10):
        line_width = 4 if i % 3 == 0 else 1
        pygame.draw.line(WIN, BLACK, (i * 60, 0), (i * 60, 540), line_width)
        pygame.draw.line(WIN, BLACK, (0, i * 60), (540, i * 60), line_width)

def draw_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                value = FONT.render(str(board[i][j]), True, BLUE)
                WIN.blit(value, (j * 60 + 20, i * 60 + 15))

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        draw_grid()
                        draw_board(board)
                        pygame.display.update()
                        time.sleep(0.05)

                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                        draw_grid()
                        draw_board(board)
                        pygame.display.update()
                        time.sleep(0.05)
                return False
    return True

def main():
    running = True
    solved = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not solved:
                    solve_sudoku(board)
                    solved = True

        draw_grid()
        draw_board(board)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
