# String to grid converter
def string_to_grid(s: str, rows: int, cols: int) -> list:
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(s[i*cols + j])
        grid.append(row)
    return grid

# Helper function to print the Sudoku grid
def print_sudoku(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()


# Function to find an empty cell in the Sudoku grid
def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None


# Function to check if a number is valid in a given position
def is_valid(grid, row, col, num):
    # Check row
    for j in range(9):
        if grid[row][j] == num:
            return False

    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[box_row + i][box_col + j] == num:
                return False

    return True


# Function to solve the Sudoku grid using backtracking
def solve_sudoku(grid):
    # Find an empty cell
    cell = find_empty_cell(grid)
    if cell is None:
        # If all cells are filled, return True to indicate success
        return True

    row, col = cell

    # Try all possible numbers in the empty cell
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            # If the number is valid, set it in the grid
            grid[row][col] = num

            # Recursively solve the remaining grid
            if solve_sudoku(grid):
                return True

            # If the remaining grid can't be solved with the current number,
            # reset the cell to 0 and try the next number
            grid[row][col] = 0

    # If none of the numbers work, backtrack
    return False


# Sample Sudoku grid to solve
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

'''
s = input("Podaj wszystkie liczby w sudoku zamieniając puste miejsca na 0: ")
grid = string_to_grid(s, 9, 9)
'''

# Solve the Sudoku grid
if solve_sudoku(grid):
    print("Solved Sudoku:")
    print_sudoku(grid)
else:
    print("No solution exists")