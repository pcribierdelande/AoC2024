import math


def read_input(input_file: str) -> tuple[list[int], list[list[int]]]:
    with open(input_file, encoding='utf8') as f:
        content = f.readlines()
        middle = content.index("\n")
        constraints = [cont[:-1].split("|") for cont in content[:middle]]
        orderings = [cont[:-1].split(",") for cont in content[middle + 1 :]]
    return constraints, orderings


def check_ordering(ordering: list[int], constraints: list[int]) -> bool:
    for constraint in constraints:
        if constraint[0] in ordering and constraint[1] in ordering:
            if ordering.index(constraint[0]) > ordering.index(constraint[1]):
                return False
    return True


def get_middle_element_from_ordering(ordering: list[int]) -> int:
    return int(ordering[math.floor(len(ordering) / 2)])


def reorder(ordering: list[int], constraints: list[int]) -> list[int]:
    for constraint in constraints:
        if constraint[0] in ordering and constraint[1] in ordering:
            i0 = ordering.index(constraint[0])
            i1 = ordering.index(constraint[1])
            if i0 > i1:
                item = ordering.pop(i0)
                if i1 == 0:
                    ordering.insert(0, item)
                else:
                    ordering.insert(i1 - 1, item)
    return ordering


def level1(orderings: list[list[int]], constraints: list[int]) -> int:
    res = 0
    for ordering in orderings:
        if check_ordering(ordering, constraints):
            res += get_middle_element_from_ordering(ordering)
    return res


def level2(orderings: list[list[int]], constraints: list[int]) -> int:
    res = 0
    for ordering in orderings:
        if not check_ordering(ordering, constraints):
            while not check_ordering(ordering, constraints):
                reorder(ordering, constraints)
            res += get_middle_element_from_ordering(ordering)
    return res


def main():
    input_file = "./Day05/input1.txt"
    constraints, orderings = read_input(input_file=input_file)

    print("level 1 : ", level1(orderings, constraints))
    print("level 2 : ", level2(orderings, constraints))


if __name__ == "__main__":
    main()
