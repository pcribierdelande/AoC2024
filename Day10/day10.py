import numpy as np


def read_input(input_file: str) -> np.ndarray[int, int]:
    with open(input_file, encoding="utf8") as f:
        content = f.readlines()
    return np.array([list(cont)[:-1] for cont in content]).astype(int)


def find_possible_end_trail(
    position: tuple[int, int], topo_map: np.ndarray[int, int]
) -> list[tuple[int, int]]:
    x, y = position
    current_height = topo_map[x, y]

    if current_height == 9:
        return [position]

    next_positions = []
    if x > 0:
        if topo_map[x - 1, y] - current_height == 1:
            next_positions.append((x - 1, y))
    if x < topo_map.shape[0] - 1:
        if topo_map[x + 1, y] - current_height == 1:
            next_positions.append((x + 1, y))
    if y > 0:
        if topo_map[x, y - 1] - current_height == 1:
            next_positions.append((x, y - 1))
    if y < topo_map.shape[1] - 1:
        if topo_map[x, y + 1] - current_height == 1:
            next_positions.append((x, y + 1))

    if len(next_positions) == 0:
        return []
    else:
        res = []
        for a in next_positions:
            res += find_possible_end_trail(a, topo_map)
        return res


def find_possible_trails(
    position: tuple[int, int], topo_map: np.ndarray[int, int]
) -> list[tuple[int, int]]:
    x, y = position
    current_height = topo_map[x, y]

    if current_height == 9:
        return 1

    next_positions = []
    if x > 0:
        if topo_map[x - 1, y] - current_height == 1:
            next_positions.append((x - 1, y))
    if x < topo_map.shape[0] - 1:
        if topo_map[x + 1, y] - current_height == 1:
            next_positions.append((x + 1, y))
    if y > 0:
        if topo_map[x, y - 1] - current_height == 1:
            next_positions.append((x, y - 1))
    if y < topo_map.shape[1] - 1:
        if topo_map[x, y + 1] - current_height == 1:
            next_positions.append((x, y + 1))

    if len(next_positions) == 0:
        return 0
    else:
        return sum([find_possible_trails(a, topo_map) for a in next_positions])


def level1(topo_map: np.ndarray[int, int]) -> int:
    res = 0
    xs, ys = np.where(topo_map == 0)
    start_zeroes = [(x, y) for x, y in zip(xs, ys)]
    for start in start_zeroes:
        end_trails = find_possible_end_trail(start, topo_map)
        res += len(set(end_trails))
    return res


def level2(topo_map: np.ndarray[int, int]) -> int:
    res = 0
    xs, ys = np.where(topo_map == 0)
    start_zeroes = [(x, y) for x, y in zip(xs, ys)]
    for start in start_zeroes:
        res += find_possible_trails(start, topo_map)
    return res


def main():
    input_file = "./Day10/input1.txt"

    topo_map = read_input(input_file)

    print("level 1 : ", level1(topo_map))
    print("level 2 : ", level2(topo_map))


if __name__ == "__main__":
    main()
