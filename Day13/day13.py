import re

pattern = r"\+?(\d+)"


def read_input(input_file: str) -> list[tuple[int, int, int, int, int, int]]:
    with open(input_file, encoding="utf8") as f:
        content = f.readlines()
    content = "".join(content)
    machines_string = content.split("\n\n")
    machines = []
    for machine_string in machines_string:
        machines.append([int(a) for a in re.findall(pattern, machine_string)])
    return machines


# def test_all_possibilities(
#     machine: tuple[int, int, int, int, int, int]
# ) -> tuple[int, int]:
#     ax, ay, bx, by, px, py = machine
#     best_a, best_b = None, None
#     min_objective = float("inf")

#     for b in range(10000000000000):
#         a = (px - b * bx) / ax
#         if a.is_integer() and 3 * a + b < min_objective:
#             best_a = a
#             best_b = b
#             min_objective = 3 * a + b

#     if not a is None:
#         return best_a, best_b
#     else:
#         return 0, 0


def compute_push_buttons(
    machine: tuple[int, int, int, int, int, int]
) -> tuple[int, int]:
    ax, ay, bx, by, px, py = machine
    num = bx * ay - by * ax

    # if num == 0:
    #     return test_all_possibilities(machine)

    b_button = (ay * px - ax * py) / num
    a_button = (by * px - bx * py) / (-num)

    if a_button.is_integer() and b_button.is_integer():
        return int(a_button), int(b_button)
    else:
        return 0, 0


def level1(machines: list[tuple[int, int, int, int, int, int]]) -> int:
    res = 0
    for machine in machines:
        a, b = compute_push_buttons(tuple(machine))
        res += 3 * a + b

    return res


def level2(machines: list[tuple[int, int, int, int, int, int]]) -> int:
    res = 0
    for machine in machines:
        machine[4] += 10000000000000
        machine[5] += 10000000000000
        a, b = compute_push_buttons(tuple(machine))
        res += 3 * a + b

    return res


def main():
    input_file = "./Day13/input1.txt"

    machines = read_input(input_file)

    print("level 1 : ", level1(machines))
    print("level 2 : ", level2(machines))


if __name__ == "__main__":
    main()
