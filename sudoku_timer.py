import os
import time
from multiprocessing import Pool

import matplotlib.pyplot as plt
import numpy as np

from sudoku import is_complete, is_valid, solve
from utils import read_sudokus


def solve_one(args):
    solve_fn, sudoku, key = args
    print(f'Starting {key}...\n')
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

    with Pool(os.cpu_count()) as p:
        times = p.map(solve_one, sudokus)       

    total_duration = sum(times)
    print(f'Solved all sudokus in {round(total_duration, 4)}s.')
    print(f'Average solving time: {round(total_duration/len(sudokus), 4)}s.')

    plt.hist(times, bins=50)
    plt.show()

    plt.hist(times, bins=np.linspace(0, 1, 50))
    plt.show()


def main():
    time_solver(solve)

if __name__ == '__main__':
    main()
