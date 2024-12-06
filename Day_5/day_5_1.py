import math

def check_ordering(ordering, constraints):
    for constraint in constraints:
        if constraint[0] in ordering and constraint[1] in ordering:
            if ordering.index(constraint[0]) > ordering.index(constraint[1]):
                return False
    return True

def get_middle(ordering):
    return int(ordering[math.floor(len(ordering)/2)])

if __name__ == "__main__":

    # Define the file's name.
    input_file = './Day_5/input_1.txt'

    # Open the file and read its content.
    with open(input_file) as f:
        content = f.readlines()
        middle = content.index('\n')
        constraints = [cont[:-1].split('|') for cont in content[:middle]]
        orderings = [cont[:-1].split(',') for cont in content[middle + 1:]]

    res = 0

    for ordering in orderings:
        if check_ordering(ordering, constraints):
            res += get_middle(ordering)
    print(res)                
