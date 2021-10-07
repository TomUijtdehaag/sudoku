from sudoku import solve, is_valid, is_complete
from utils import read_sudokus

import time

def time_solver(solve_fn):
    sudokus = read_sudokus('puzzles.txt')

    total_start = time.time()

    for key, sudoku in sudokus.items():
        print(f'Solving {key}')
        single_start = time.time()
        solution = solve_fn(sudoku)
        single_duration = time.time() - single_start
        print(f'Done in {round(single_duration, 4)}s.\nSolution:')
        print(solution)
        print(f'Solution is valid: {is_valid(solution)}')
        print(f'Solution is complete: {is_complete(solution)}')
        print('\n')


    total_duration = time.time() - total_start
    print(f'Solved all sudokus in {round(total_duration, 4)}s.')
    print(f'Average solving time: {round(total_duration/50, 4)}s.')


def main():
    time_solver(solve)

if __name__ == '__main__':
    main()