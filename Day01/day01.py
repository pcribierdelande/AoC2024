def read_input(input_file: str) -> tuple[list[int], list[int]]:
    with open(input_file, encoding='utf8') as f:
        content = f.readlines()

    left_list = []
    right_list = []

    for line in content:
        temp = line.split("\n")[0].split(" ")
        left_list.append(int(temp[0]))
        right_list.append(int(temp[-1]))

    return left_list, right_list


def level1(list1: list, list2: list) -> int:
    res = 0
    for a, b in zip(sorted(list1), sorted(list2)):
        res += abs(a - b)
    return res


def level2(list1: list, list2: list) -> int:
    res = 0
    for a in list1:
        res += list2.count(a) * a
    return res


def main():
    input_file = "./Day01/input1.txt"

    left_list, right_list = read_input(input_file)

    print("level 1 : ", level1(list1=left_list, list2=right_list))
    print("level 2 : ", level2(list1=left_list, list2=right_list))

if __name__ == "__main__":
    main()
