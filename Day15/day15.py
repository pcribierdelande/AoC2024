def read_input(input_file: str) -> tuple:
    with open(input_file, encoding="utf8") as f:
        content = f.readlines()
    return content


def level1() -> int:
    res = 0

    return res


def level2() -> int:
    res = 0

    return res


def main():
    input_file = "./Day15/input0.txt"

    _ = read_input(input_file)

    print("level 1 : ", level1())
    print("level 2 : ", level2())


if __name__ == "__main__":
    main()
