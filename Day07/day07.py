from itertools import product 

def read_input(input_file: str) -> list[str]:

    result = []
    with open(input_file) as f:
        for line in f.readlines():
            colons_split = line.split(':')
            c = colons_split[1].strip().split(' ')
            result.append(colons_split[:1] + c)
    return result


def read_equation(equation: list, operator: list) -> int:
    current = str(eval(equation[0] + operator[0] + equation[1]))
    for nbr, op in zip(equation[2:], operator[1:]):
        current = str(eval(current + op + nbr))
    return int(current)


def generate_all_combination_of_operators(length_equation: int, operators: list[str]) -> list[list[str]]:
    return [list(i) for i in product(operators, repeat=length_equation-1)]


def check_equation_can_be_ok(equation: list[str], operators: list[str]) -> bool:
    expected = int(equation[0])
    right_hand = equation[1:]
    all_possible_ops = generate_all_combination_of_operators(len(right_hand), operators)
    for ops in all_possible_ops:
        if read_equation(right_hand, ops) == expected:
            return True
    return False


def check_all_equations(equations: list[str], operators: list[str]) -> int:
    res = 0

    for equation in equations:
        if check_equation_can_be_ok(equation, operators):
            res += int(equation[0])

    return res

def level1(equations: list) -> int:
    return check_all_equations(equations,  ['*', '+'])


def level2(equations: list) -> int:
    return check_all_equations(equations,  ['*', '+', ''])


if __name__ == "__main__":
    input_file = './Day07/input1.txt'

    equations = read_input(input_file)

    print('level 1 : ', level1(equations=equations))
    print('level 2 : ', level2(equations=equations))
