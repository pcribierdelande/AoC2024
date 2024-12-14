import math
import re

import matplotlib.pyplot as plt
import numpy as np

pattern = r"(-?\d+)"

def read_input(input_file: str) -> list[list[int, int], tuple[int, int]]:
    with open(input_file, encoding="utf8") as f:
        content = f.readlines()
    robots = []
    for cont in content:
        tmp  = re.findall(pattern, cont)
        robots.append([int(tmp[1]), int(tmp[0]), (int(tmp[3]), int(tmp[2]))])
    return robots

def print_numpy(grid: np.ndarray[str, str]):
    grid = grid.astype(str)
    grid[grid == '0'] = '.'
    for line in grid:
        print(''.join(line))


def get_grid(robots: list[list[int, int, tuple[int, int]]], x_lim: int, y_lim: int) -> np.ndarray[int, int]:
    grid = np.zeros((x_lim, y_lim)).astype(int)
    for robot in robots:
        grid[robot[0], robot[1]] += 1

    return grid

def get_pos_after_n_steps(robot: list[int, int, tuple[int, int]], n: int, x_lim: int, y_lim: int) -> list[int, int, tuple[int, int]]:
    x, y, v = robot
    x = (x + n * v[0]) % x_lim
    y = (y + n * v[1]) % y_lim
    return [x, y, v]


def extract_quarter(grid: np.ndarray[int, int]) -> list[np.ndarray[int, int]]:
    x_middle = math.floor(grid.shape[0] / 2)
    y_middle = math.floor(grid.shape[1] / 2)

    upper_left = grid[:x_middle, :y_middle]
    upper_right = grid[:x_middle, y_middle + 1:]
    lower_left = grid[x_middle+1:, :y_middle]
    lower_right = grid[x_middle+1:, y_middle+1:]
    return [upper_left, upper_right, lower_left, lower_right]


def get_score(grid: np.ndarray[int, int]) -> int:
    res = 1
    quarters = extract_quarter(grid)
    for quarter in quarters:
        res *= quarter[quarter != 0].sum()
    return res


def find_runs(line: np.ndarray[int], length: int):
    kernel = np.ones(length)
    conv = np.convolve(line, kernel, mode='valid')
    return np.where(conv == length)[0]


def check_square(grid: np.ndarray[int, int]) -> bool:
    row_number = 0
    for i, row in enumerate(grid):
        runs = find_runs(row, 10)
        row_number += len(runs)

    col_number = 0
    for j in range(grid.shape[1]):
        col = grid[:, j]
        runs = find_runs(col, 10)
        col_number += len(runs)

    return row_number >= 2 and col_number >= 2



def level1(robots: list[list[int, int, tuple[int, int]]], x_lim: int, y_lim: int) -> int:
    final_pos = []
    for robot in robots:
        robot = get_pos_after_n_steps(robot, 7138, x_lim, y_lim)
        final_pos.append(robot)
    array = get_grid(final_pos, x_lim, y_lim)
    return get_score(array)


def level2(robots: list[list[int, int, tuple[int, int]]], x_lim: int, y_lim: int) -> int:
    cur_pos = robots.copy()

    for i in range(10000000000):
        next_pos = []
        for robot in cur_pos:
            robot1 = get_pos_after_n_steps(robot, 1, x_lim, y_lim)
            next_pos.append(robot1)

        array = get_grid(next_pos, x_lim, y_lim)
        if check_square(array):
            plt.figure(figsize=(20, 20))
            plt.imshow(1-array, cmap='binary')
            return i + 1
        cur_pos = next_pos
    

def main():
    input_file = "./Day14/input1.txt"
    x_lim = 103
    y_lim = 101

    robots = read_input(input_file)
    print("level 1 : ", level1(robots, x_lim, y_lim))
    print("level 2 : ", level2(robots, x_lim, y_lim))
    plt.show()


if __name__ == "__main__":
    main()
