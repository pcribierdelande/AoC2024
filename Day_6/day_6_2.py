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


def arpenter(current, direction, x_lim, y_lim, obstacles, history):
    # print(current, direction, x_lim, y_lim, obstacles, history)
    infinite = False
    path = history + [(current, direction)]
    while not check_finish(current, x_lim, y_lim):
        current, direction = get_next(current, direction, obstacles)
        if (current, direction) in path:
            infinite = True
            # print('*******************')
            break
        path.append((current, direction))
    return infinite, path


if __name__ == "__main__":

    # Define the file's name.
    input_file = './Day_6/input_1.txt'

    # Open the file and read its content.
    with open(input_file) as f:
        content = f.readlines()
        grid = np.array([list(a)[:-1] for a in content])

    x_lim, y_lim = grid.shape
    start = np.where(grid == '^')
    start = (start[0][0], start[1][0])

    xo, yo = np.where(grid == '#')
    obstacles = [(x,y) for x,y in zip(xo, yo)]

    _, path = arpenter(start, 'U', x_lim, y_lim, obstacles, [])

    print(len(set([a[0] for a in path]))-1)

    possibles = []

    # print(path)

    for i in range(len(path)-2):
        # print('_______________________________')
        if i % 10 == 0:
            print(i)
        infinite, _ = arpenter(path[i][0], path[i][1], x_lim, y_lim, obstacles + [path[i+1][0]], path[:i])
        if infinite:
            possibles.append(path[i+1][0])

    # print(possibles)
    print(len(possibles))
    print(len(set(possibles)))

# 1695 too low
# 2094 too high
# 1941, 1940
