import os
import curses

grid_size = int(input("Enter grid size: "))
def draw(stdscr, grid):
    stdscr.erase()
    for r, row in enumerate(grid):
        stdscr.addstr(r, 0, " ".join(row))
    stdscr.refresh()

def initialize_snake(grid):
    grid[0][0] = "0"

def move_up(grid, row, col):
    row = row - 1
    grid[row][col] = "0"
    return row, col

def move_down(grid, row, col):
    row = row + 1
    grid[row][col] = "0"
    return row, col

def move_left(grid, row, col):
    col = col - 1
    grid[row][col] = "0"
    return row, col

def move_right(grid, row, col):
    col = col + 1
    grid[row][col] = "0"
    return row, col

def main(stdscr):
    stdscr.nodelay(True)
    stdscr.timeout(100)
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
    row = 0
    col = 0
    initialize_snake(grid)
    while True:
        draw(stdscr, grid) 
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == ord('s'):
            row, col = move_down(grid, row, col)
        elif key == ord('d'):
            row, col = move_right(grid, row, col)
        else:
            pass


curses.wrapper(main)
