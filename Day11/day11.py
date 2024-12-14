from functools import cache
from operator import itemgetter


def read_input(input_file: str) -> list[int]:
    with open(input_file, encoding="utf8") as f:
        content = f.readlines()
    return [int(a) for a in content[0].split(" ")]


def one_blink(stones_line: list[int]) -> list[int]:
    new_line = []
    for stone in stones_line:
        if stone == 0:
            new_line.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            new_line.append(int(stone_str[: int(len(stone_str) / 2)]))
            new_line.append(int(stone_str[int(len(stone_str) / 2) :]))
        else:
            new_line.append(stone * 2024)
    return new_line

@cache
def stones_after_blinks(stone: int, blinks: int) -> None:
    if blinks == 1:
        if (stone, 1) not in dict_stones:
            dict_stones[(stone, 1)] = one_blink([stone])

    if (stone, blinks) not in dict_stones:
        next_stones = one_blink([stone])
        dict_stones[(stone, blinks)] = [(a, blinks - 1) for a in next_stones]
        for a in next_stones:
            stones_after_blinks(a, blinks - 1)


def fill_dict():
    list_keys = list(dict_stones.keys())
    list_keys.sort(key=itemgetter(1))
    for key in list_keys:
        if isinstance(dict_stones[key], int):
            pass
        elif isinstance(dict_stones[key][0], int):
            dict_stones[key] = len(dict_stones[key])
        elif isinstance(dict_stones[key][0], tuple):
            dict_stones[key] = sum([dict_stones[a] for a in dict_stones[key]])


def level1(stones_line: list[int]) -> int:
    for _ in range(25):
        stones_line = one_blink(stones_line)

    return len(stones_line)


def level2(stones_line) -> int:
    res = 0
    for stone in stones_line:
        stones_after_blinks(stone, 75)

    fill_dict()

    for stone in stones_line:
        res += dict_stones[(stone, 75)]
    return res


def main():
    input_file = "./Day11/input1.txt"

    stones_line = read_input(input_file)

    print("level 1 : ", level1(stones_line))
    print("level 2 : ", level2(stones_line))


if __name__ == "__main__":
    dict_stones = {}

    main()
