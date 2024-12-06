import numpy as np


def next_direction(direction):
    match direction:
        case 'U':
            return 'R'
        case 'R':
            return 'D'
        case 'L':
            return 'U'
        case 'D':
            return 'L'

def compute_next(current, direction):
    x,y = current
    match direction:
        case 'U':
            return (x-1, y)
        case 'R':
            return (x, y+1)
        case 'L':
            return (x, y-1)
        case 'D':
            return (x+1, y)


def get_next(current, direction, obstacles):

    new = compute_next(current, direction)
    while new in obstacles:
        direction = next_direction(direction)
        new = compute_next(current, direction)

    return new, direction


def check_finish(new, x_lim, y_lim):
    x,y = new

    return (x < 0 or y < 0 or x >= x_lim or y >= y_lim)

def arpenter(current, direction, x_lim, y_lim, obstacles):
    path = [current]

    while not check_finish(current, x_lim, y_lim):
        current, direction = get_next(current, direction, obstacles)
        path.append(current)
    return path

if __name__ == "__main__":

    # Define the file's name.
    input_file = './Day_6/input_1.txt'

    # Open the file and read its content.
    with open(input_file) as f:
        content = f.readlines()
        grid = np.array([list(a)[:-1] for a in content])

    x_lim, y_lim = grid.shape
    current = np.where(grid == '^')
    current = (current[0][0], current[1][0])
    direction = 'U'
    xo, yo = np.where(grid == '#')
    obstacles = [(x,y) for x,y in zip(xo, yo)]

    path = arpenter(current, direction, x_lim, y_lim, obstacles)

    print(len(set(path)) - 1)
