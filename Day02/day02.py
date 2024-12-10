import numpy as np


def read_input(input_file: str) -> list:
    readings = []
    with open(input_file, encoding='utf8') as f:
        for line in f.readlines():
            temp = line.split("\n")[0].split(" ")
            reading = [int(a) for a in temp]
            readings.append(reading)
    return readings


def check_reading_safe(reading_diff: np.array) -> bool:
    if 0 in reading_diff:
        return False
    elif (-3 > reading_diff).any() or (3 < reading_diff).any():
        return False
    elif (0 > reading_diff).all() or (0 < reading_diff).all():
        return True
    else:
        return False


def level1(readings: list) -> int:
    res = 0
    for reading in readings:
        diff_list = np.diff(reading)
        res += check_reading_safe(diff_list)
    return res


def level2(readings: list) -> int:
    res = 0

    for reading in readings:
        diff_list = np.diff(reading)

        if check_reading_safe(diff_list):
            res += 1
        else:
            for a in range(len(reading)):
                diff_list = np.diff(reading[:a] + reading[a + 1 :])
                if check_reading_safe(diff_list):
                    res += 1
                    break
    return res

def main():

    input_file = "./Day02/input1.txt"
    readings = read_input(input_file=input_file)

    print(level1(readings=readings))
    print(level2(readings=readings))

if __name__ == "__main__":
    main()
