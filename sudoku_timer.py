from multiprocessing import Pool

from sudoku import solve, is_valid, is_complete
from utils import read_sudokus

import time

def solve_one(args):
    solve_fn, sudoku, key = args
    print(f'Starting {key}...')
    single_start = time.time()
    solution = solve_fn(sudoku)
    single_duration = time.time() - single_start
    print(f'Solved {key} in {round(single_duration, 4)}s.\nSolution:')
    print(solution)
    print(f'Solution is valid: {is_valid(solution)}')
    print(f'Solution is complete: {is_complete(solution)}')
    print('\n')
    return single_duration

def time_solver(solve_fn):
    sudokus = read_sudokus('puzzles.txt')
    sudokus = [(solve_fn, sudoku, key) for key, sudoku in sudokus.items()]

    with Pool(16) as p:
        times = p.map(solve_one, sudokus)       

    total_duration = sum(times)
    print(f'Solved all sudokus in {round(total_duration, 4)}s.')
    print(f'Average solving time: {round(total_duration/len(sudokus), 4)}s.')


def main():
    time_solver(solve)

if __name__ == '__main__':
    main()