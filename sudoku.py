import numpy as np

from utils import read_sudokus


def solve(grid):
    if is_complete(grid):
        return grid

    best_option, possible_numbers = rank_options(grid)
    if len(possible_numbers) == 0:
        return grid

    new_grid = grid.copy()
  
    for number in possible_numbers:
        new_grid[best_option[0], best_option[1]] = number

        new_grid = solve(new_grid)
        
        if is_complete(new_grid):
            return new_grid

    return grid


def get_options(grid):
    return np.argwhere(grid == 0)

def rank_options(grid):
    subsize = int(len(grid)**.5)
    options = get_options(grid)
    possible_list = []

    for i, j in options:
        possible = set(range(1,len(grid)+1))
        banned = set(
            grid[i].tolist() + 
            grid[:,j].tolist() + 
            grid[(i//subsize)*subsize:(i//subsize+1)*subsize,(j//subsize)*subsize:(j//subsize+1)*subsize].flatten().tolist()
            )

        possible -= banned
        
        possible_list.append(possible)

    best = np.argmin([len(p) for p in possible_list])
    if len(possible_list[best]) == 0: return None, set()

    best_option = options[best]
    possible_numbers = possible_list[best]

    return best_option, possible_numbers

        
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
    key = 'Grid 26'
    sudoku = sudokus[key]
    print('Solving', key)
    solution = solve(sudoku)
    print(np.matrix(solution))

if __name__ == '__main__':
    main()
