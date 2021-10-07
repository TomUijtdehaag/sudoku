import numpy as np

def read_sudokus(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
    
    sudokus = {}
    for i in range(0, len(lines), 10):
        key = lines[i]
        puzzle = []
        for line in lines[i+1:i+10]:
            puzzle.append([int(v) for v in line])

        sudokus[key] = np.array(puzzle)

    return sudokus