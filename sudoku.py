import numpy as np

from utils import read_sudokus


def solve(grid):
    if is_complete(grid):
        return grid

    choice = get_options(grid)[0]
    new_grid = grid.copy()

    for val in range(1, len(grid)+1):
        new_grid[choice[0], choice[1]] = val

        if is_valid(new_grid):
            new_grid = solve(new_grid)
            
            if is_complete(new_grid):
                return new_grid

    return grid


def get_options(grid):
    return np.argwhere(grid == 0)

        
def is_valid(grid):
    size = len(grid)
    sub_size = int(size**.5)
    for val in range(1,size+1):
        # check rows
        for row in grid:
            if len(np.argwhere(row==val)) > 1:
                return False

        # check columns
        for col in grid.T:
            if len(np.argwhere(col==val)) > 1:
                return False

        # check subgrids
        indices = list(range(0, size+1, sub_size))
        for i in range(sub_size):
            row_start, row_end = indices[i], indices[i+1]

            for j in range(sub_size):
                col_start, col_end = indices[j], indices[j+1]

                subgrid = grid[row_start:row_end, col_start:col_end]

                if len(np.argwhere(subgrid==val)) > 1:
                    return False
            
    return True

def is_complete(grid):
    if len(np.argwhere(grid == 0)) == 0:
        return True
    else:
        return False

def main():
    sudokus = read_sudokus('puzzles.txt')
    key = 'Grid 01'
    sudoku = sudokus[key]
    print('Solving', key)
    solution = solve(sudoku)
    print(np.matrix(solution))

if __name__ == '__main__':
    main()
