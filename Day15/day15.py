import numpy as np


def read_input(input_file: str) -> tuple:
    with open(input_file, encoding="utf8") as f:
        content = f.readlines()
    a = ''.join(content).split('\n\n')
    grid = a[0].split('\n')
    instructions = ''.join(a[1].split('\n'))
    return grid, instructions



def print_grid1(obstacles, boxes, robot, shape):
    grid = np.full(shape, '.')
    for obstacle in obstacles:
        grid[obstacle] = '#'
    for box in boxes:
        grid[tuple(box)] = 'O'
    grid[robot] = '@'
    
    print('____________')
    for row in grid:
        print(''.join(row))
    print('____________')


def print_grid2(obstacles, boxes, robot, shape):
    grid = np.full(shape, '.')
    for obstacle in obstacles:
        grid[obstacle] = '#'
    for box in boxes:
        grid[tuple(box)] = '['
        grid[box[0], box[1]+ 1] = ']'
    grid[robot] = '@'
    
    print('____________')
    for row in grid:
        print(''.join(row))
    print('____________')



def get_info_from_grid(grid : np.ndarray) -> tuple[list[tuple[int, int]], list[tuple[int, int]], tuple[int, int]]:
    obstacles = []
    xs, ys = np.where(grid == '#')
    for x, y in zip(xs, ys):
        obstacles.append((int(x),int(y)))

    boxes = []

    if 'O' in grid:
        xs, ys = np.where(grid == 'O')
        for x, y in zip(xs, ys):
            boxes.append((int(x),int(y)))
    else:
        xs, ys = np.where(grid == '[')
        for x, y in zip(xs, ys):
            boxes.append((int(x),int(y)))

    x_r, y_r = np.where(grid == '@')
    robot = (int(x_r[0]), int(y_r[0]))

    return obstacles, boxes, robot

def get_mouvement(robot: tuple[int, int], instruction: str):
    x, y = robot
    match instruction:
        case '^':
            return x-1, y
        case '>':
            return x, y + 1
        case '<':
            return x , y-1
        case 'v':
            return x+1, y


def get_next_step(obstacles: list[tuple[int, int]], boxes: list[tuple[int, int]], robot: tuple[int, int], instruction: str):
    possible_next_pos = get_mouvement(robot, instruction)
    if possible_next_pos in obstacles:
        return boxes, robot
    elif possible_next_pos in boxes:
        box_to_move = possible_next_pos
        to_move = boxes.index(possible_next_pos)
        while box_to_move in boxes:
            box_to_move = get_mouvement(box_to_move, instruction)
            if box_to_move in obstacles:
                return boxes, robot
            else:
                to_add = box_to_move
        assert box_to_move not in obstacles and box_to_move not in boxes
        boxes.pop(to_move)
        boxes.append(to_add)
        return boxes, possible_next_pos
    else:
        return boxes, possible_next_pos


def get_score(boxes: list[tuple[int, int]]) -> int:
    res = 0
    for box in boxes:
        res += 100 * box[0] + box[1]
    return res 


def level1(grid: np.ndarray[str, str], instructions: str) -> int:
    shape = grid.shape
    obstacles, boxes, robot = get_info_from_grid(grid)
    for instruction in instructions:
        boxes, robot = get_next_step(obstacles, boxes, robot, instruction)

    return get_score(boxes)


def level2(grid: np.ndarray[str, str], instructions: str) -> int:
    res = 0
    shape = grid.shape
    obstacles, boxes, robot = get_info_from_grid(grid)

    print_grid2(obstacles, boxes, robot, shape)
    obstacles, boxes, robot = get_info_from_grid(grid)
    return res


def main():
    input_file = "./Day15/input0.txt"

    grid, instructions = read_input(input_file)
    grid1 = np.array([list(row) for row in grid])
    grid2 = np.array([list(row.replace("#", "##").replace('.', '..').replace('@', '@.').replace('O', '[]')) for row in grid])

    print("level 1 : ", level1(grid1, instructions))
    print("level 2 : ", level2(grid2, instructions))


if __name__ == "__main__":
    main()
