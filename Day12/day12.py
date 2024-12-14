import math
from functools import cache

import numpy as np


def read_input(input_file: str) -> np.ndarray[str, str]:
    with open(input_file, encoding="utf8") as f:
        content = f.readlines()
    return np.array([list(cont[:-1]) for cont in content])


def get_possible_neighbours(
    x: int, y: int, x_min: int, y_min: int, x_max: int, y_max: int
) -> list[tuple[int, int]]:
    neighbours = []
    if x > x_min:
        neighbours.append((x - 1, y))
    if y > y_min:
        neighbours.append((x, y - 1))
    if x < x_max:
        neighbours.append((x + 1, y))
    if y < y_max:
        neighbours.append((x, y + 1))
    return neighbours


def fill_region(start: tuple[int, int], grid: np.ndarray[str, str]) -> list[int]:
    global visited

    x, y = start

    if (x, y) in visited:
        return []

    visited.append((x, y))

    neighbours = get_possible_neighbours(
        x, y, 0, 0, grid.shape[0] - 1, grid.shape[1] - 1
    )

    for neighbour in neighbours:
        if grid[neighbour] == grid[start]:
            fill_region(neighbour, grid)
    return visited


def get_regions(value: str, grid: np.ndarray[str, str]) -> tuple[set[tuple[int, int]]]:
    global visited

    xs, ys = np.where(grid == value)
    regions = []
    coord = {(x, y) for x, y in zip(xs, ys)}
    while len(coord) != 0:
        start = coord.pop()
        visited = []
        region = fill_region(start, grid)
        regions.append(region)
        coord = coord - set(region)
    return regions


def get_price_without_bulk(
    region: list[tuple[int, int]], grid: np.ndarray[str, str]
) -> int:
    aire = len(region)
    perimeter = 4 * aire
    for coord in region:
        neighbours = get_possible_neighbours(
            coord[0], coord[1], 0, 0, grid.shape[0] - 1, grid.shape[1] - 1
        )
        perimeter -= len(set(region).intersection(set(neighbours)))

    return aire * perimeter


def get_fences(
    region: list[tuple[int, int]], grid: np.ndarray[str, str]
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    fences = []
    for coord in region:
        neighbours = get_possible_neighbours(
            coord[0], coord[1], -1, -1, grid.shape[0], grid.shape[1]
        )
        fences += [(coord, nei) for nei in neighbours if nei not in region]

    return fences


def split_fences_orientation(
    fences: list[tuple[tuple[int, int], tuple[int, int]]]
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:

    horizontal_fences = []
    vertical_fences = []
    for fence in fences:
        (x1, y1), (x2, y2) = fence
        if x1 == x2:
            vertical_fences.append((x1, ((y1 + y2) / 2)))
        else:
            horizontal_fences.append((y1, (x1 + x2) / 2))
    return horizontal_fences, vertical_fences


def group_by_second(fences: list[tuple[int, int]]) -> dict[int : list[int]]:
    res = {}
    for x, y in fences:
        if y in res:
            res[y].append(x)
        else:
            res[y] = [x]
    return res


def get_number_of_bulk_fences(
    fences: list[tuple[int, int]], hori: bool, value: str, grid: np.ndarray[str, str]
) -> int:
    res = 0
    dict_fence = group_by_second(fences)
    for k, list_fence in dict_fence.items():
        list_fence = sorted(list_fence)
        if len(list_fence) == 1:
            res += 1
        else:
            sequencial_fences = list(np.where(np.diff(list_fence) > 1)[0])
            sequencial_fences.append(len(list_fence) - 1)
            before = math.floor(k)
            after = math.ceil(k)

            if (
                (after > grid.shape[0] - 1 and hori)
                or (after > grid.shape[1] - 1 and not hori)
                or (before < 0)
            ):
                res += len(sequencial_fences)

            else:
                begining = 0

                for hole in sequencial_fences:
                    res += 1

                    if hori:
                        in_fence = grid[before, list_fence[begining]] == value
                    else:
                        in_fence = grid[list_fence[begining], before] == value

                    for i in list_fence[begining : hole + 1]:
                        if hori:
                            if grid[before, i] == value and not in_fence:
                                in_fence = True
                                res += 1
                            elif grid[after, i] == value and in_fence:
                                in_fence = False
                                res += 1
                        else:
                            if grid[i, before] == value and not in_fence:
                                in_fence = True
                                res += 1
                            elif grid[i, after] == value and in_fence:
                                in_fence = False
                                res += 1
                    begining = hole + 1

    return res


def get_price_with_bulk(
    region: list[tuple[int, int]], grid: np.ndarray[str, str], value: str
) -> int:
    aire = len(region)
    fences = get_fences(region, grid)
    horizontal_fences, vertical_fences = split_fences_orientation(fences)
    return (
        get_number_of_bulk_fences(horizontal_fences, True, value, grid)
        + get_number_of_bulk_fences(vertical_fences, False, value, grid)
    ) * aire


def level1(grid: np.ndarray[str, str]) -> int:
    res = 0

    for value in np.unique(grid):
        res += sum(
            [
                get_price_without_bulk(region, grid)
                for region in get_regions(value, grid)
            ]
        )
    return res


def level2(grid: np.ndarray[str, str]) -> int:
    res = 0

    for value in np.unique(grid):
        res += sum(
            [
                get_price_with_bulk(region, grid, value)
                for region in get_regions(value, grid)
            ]
        )
        print(value, res)
    return res


def main():
    input_file = "./Day12/input1.txt"

    grid = read_input(input_file)

    print("level 1 : ", level1(grid))
    print("level 2 : ", level2(grid))


if __name__ == "__main__":
    visited = []

    main()
