if __name__ == "__main__":


    # Define the file's name.
    input_file = './Day_1/input_1.txt'


    # Open the file and read its content.
    with open(input_file) as f:
        content = f.readlines()


    list_1 = []
    list_2 = []


    for line in content:
        temp = line.split('\n')[0].split(' ')
        list_1.append(int(temp[0]))
        list_2.append(int(temp[-1]))


    res = 0
    for a, b in zip(sorted(list_1), sorted(list_2)):
        res += abs(a-b)

    print(res)
