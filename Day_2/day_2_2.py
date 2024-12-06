import numpy as np


def check_line(np_list):
    if 0 in np_list:
        return 0
    elif (-3 > np_list).any() or (3 < np_list).any():
        return 0
    elif (0> np_list).all() or (0<np_list).all():
        return 1
    else:
        return 0
    
if __name__ == "__main__":

    # Define the file's name.
    input_file = './Day_2/input_1.txt'

    # Open the file and read its content.
    with open(input_file) as f:
        content = f.readlines()

    res = 0

    input_lists = []
    for line in content:
        temp = line.split('\n')[0].split(' ')
        reading = [int(a) for a in temp]
        diff_list = np.diff(reading)

        if check_line(diff_list):
            res += 1
        else:
            for a in range(len(reading)):
                diff_list = np.diff(reading[:a] + reading[a+1:])
                if check_line(diff_list):
                    res += 1
                    break

    print(res)
