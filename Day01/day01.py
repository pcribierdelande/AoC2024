def read_input(input_file: str) -> tuple[list[int], list[int]]:
    with open(input_file) as f:
        content = f.readlines()

    list1 = []
    list2 = []

    for line in content:
        temp = line.split('\n')[0].split(' ')
        list1.append(int(temp[0]))
        list2.append(int(temp[-1]))

    return list1, list2


def level1(list1: list, list2 :list) -> int:
    res = 0
    for a, b in zip(sorted(list1), sorted(list2)):
        res += abs(a-b)
    return res


def level2(list1: list, list2 :list) -> int:
    res = 0
    for a in list1:
        res += list2.count(a) * a
    return res


if __name__ == "__main__":
    input_file = './Day01/input1.txt'

    list1, list2 = read_input(input_file)

    print('level 1 : ', level1(list1=list1, list2=list2))
    print('level 2 : ', level2(list1=list1, list2=list2))
