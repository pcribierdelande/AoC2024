import numpy as np

def read_input(input_file: str) -> np.ndarray[str, str]:
    with open(input_file) as f:
        content = f.readlines()
        grid = np.array([list(a)[:-1] for a in content])
    return grid


def next_direction(direction : str) -> str:
    match direction:
        case 'U':
            return 'R'
        case 'R':
            return 'D'
        case 'L':
            return 'U'
        case 'D':
            return 'L'

def compute_next_possible_position(current_position: tuple[int, int], direction: str) -> tuple[int, int]:
    x,y = current_position
    match direction:
        case 'U':
            return (x-1, y)
        case 'R':
            return (x, y+1)
        case 'L':
            return (x, y-1)
        case 'D':
            return (x+1, y)


def get_next_guard_position(current_position: tuple[int, int], direction: str, obstacles: list[tuple[int, int]]) ->  tuple[tuple[int, int], str]:
    new_position = compute_next_possible_position(current_position, direction)
    while new_position in obstacles:
        direction = next_direction(direction)
        new_position = compute_next_possible_position(current_position, direction)

    return new_position, direction


def check_guard_outside(guard_position: tuple[int], x_lim: int, y_lim: int) -> bool:
    x,y = guard_position
    return (x < 0 or y < 0 or x >= x_lim or y >= y_lim)


def arpenter(current_position: tuple[int, int], direction: str, x_lim: int, y_lim: int, obstacles: list[tuple[int, int]], history: list[int]):
    infinite = False
    path = history + [(current_position, direction)]
    while not check_guard_outside(current_position, x_lim, y_lim):
        current_position, direction = get_next_guard_position(current_position, direction, obstacles)
        if (current_position, direction) in path:
            infinite = True
            break
        path.append((current_position, direction))
    return infinite, path


def level1(current_position: tuple[int, int], direction: str, x_lim: int, y_lim: int, obstacles: list[tuple[int, int]]) -> int:
    _, path = arpenter(current_position, direction, x_lim, y_lim, obstacles, [])
    return len({a[0] for a in path}) - 1


def level2(current_position: tuple[int, int], direction: str, x_lim: int, y_lim: int, obstacles: list[tuple[int, int]]) -> int:
    _, path = arpenter(current_position, direction, x_lim, y_lim, obstacles, [])

    possibles = []

    for i in range(len(path)-2):
        if i < 1000:
            if i%100 == 0:
                print(i)
        elif i % 1000 == 0:
            print(i)

        if path[i+1][0] not in [a[0] for a in path[:i]]:
            infinite, _ = arpenter(path[i][0], path[i][1], x_lim, y_lim, obstacles + [path[i+1][0]], path[:i])
            if infinite:
                possibles.append(path[i+1][0])

    return len(set(possibles))


if __name__ == "__main__":

    input_file = './Day06/input1.txt'

    grid = read_input(input_file)

    x_lim, y_lim = grid.shape
    start_position = np.where(grid == '^')
    current_position = (start_position[0][0], start_position[1][0])
    direction = 'U'
    xo, yo = np.where(grid == '#')
    obstacles = [(x,y) for x,y in zip(xo, yo)]

    print('level 1 : ', level1(current_position, direction, x_lim, y_lim, obstacles))
    print('level 2 : ', level2(current_position, direction, x_lim, y_lim, obstacles))
