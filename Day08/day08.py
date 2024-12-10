import itertools

import numpy as np


def read_input(input_file: str) -> tuple[np.ndarray[str, str], list[str]]:
    with open(input_file, encoding="utf8") as f:
        content = f.readlines()

    grid = np.array([list(cont) for cont in content])[:, :-1]
    all_antena_types = [a[0] for a in list(np.unique(grid)) if a[0] != "."]
    return grid, all_antena_types


def get_antinodes_from_two_antenas(
    antena1: tuple[int, int], antena2: tuple[int, int], x_lim: int, y_lim: int
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    x1, y1 = antena1
    x2, y2 = antena2
    diff_x = x1 - x2
    diff_y = y1 - y2
    possible1 = (x1 + diff_x, y1 + diff_y)
    possible2 = (x2 - diff_x, y2 - diff_y)

    possible_antinodes1 = []
    possible_antinodes2 = []
    while check_antinode_in_grid(possible1, x_lim, y_lim):
        possible_antinodes1.append(possible1)
        possible1 = (possible1[0] + diff_x, possible1[1] + diff_y)
    while check_antinode_in_grid(possible2, x_lim, y_lim):
        possible_antinodes2.append(possible2)
        possible2 = (possible2[0] - diff_x, possible2[1] - diff_y)
    return (possible_antinodes1, possible_antinodes2)


def check_antinode_in_grid(
    antinode_coord: tuple[int, int], x_lim: int, y_lim: int
) -> bool:
    x, y = antinode_coord
    return not (x < 0 or y < 0 or x >= x_lim or y >= y_lim)


def level1(
    grid: np.ndarray[str, str], all_antena_type: list[str], x_lim: int, y_lim: int
) -> int:
    antinodes = []
    for antena_type in all_antena_type:
        xs, ys = np.where(grid == antena_type)
        antena_coords = [(int(x), int(y)) for x, y in zip(xs, ys)]
        for antena_couple in list(itertools.combinations(antena_coords, 2)):
            possible1, possible2 = get_antinodes_from_two_antenas(
                antena1=antena_couple[0],
                antena2=antena_couple[1],
                x_lim=x_lim,
                y_lim=y_lim,
            )
            if len(possible1) > 0:
                antinodes.append(possible1[0])
            if len(possible2) > 0:
                antinodes.append(possible2[0])
    return len(set(antinodes))


def level2(
    grid: np.ndarray[str, str], all_antena_type: list[str], x_lim: int, y_lim: int
) -> int:
    antinodes = []
    for antena_type in all_antena_type:
        xs, ys = np.where(grid == antena_type)
        antena_coords = [(int(x), int(y)) for x, y in zip(xs, ys)]
        for antena_couple in list(itertools.combinations(antena_coords, 2)):
            possible1, possible2 = get_antinodes_from_two_antenas(
                antena1=antena_couple[0],
                antena2=antena_couple[1],
                x_lim=x_lim,
                y_lim=y_lim,
            )
            antinodes += possible1
            antinodes += possible2
        if len(antena_coords) > 1:
            antinodes += antena_coords
    return len(set(antinodes))


def main():
    input_file = "./Day08/input1.txt"

    grid, all_antena_type = read_input(input_file)
    x_lim, y_lim = grid.shape

    print("level 1 : ", level1(grid, all_antena_type, x_lim, y_lim))
    print("level 2 : ", level2(grid, all_antena_type, x_lim, y_lim))


if __name__ == "__main__":
    main()
