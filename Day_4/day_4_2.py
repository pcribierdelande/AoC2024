import numpy as np

def check_xmas(array, i, j):
    if i==0 or j==0 or i==array.shape[0]-1 or j==array.shape[1]-1:
        return 0
    search = {'M', 'S'}
    one = {array[i-1,j-1], array[i+1,j+1]}
    two = {array[i-1,j+1], array[i+1,j-1]}
    return one == search and two == search



if __name__ == "__main__":

    # Define the file's name.
    input_file = './Day_4/input_1.txt'

    # Open the file and read its content.
    with open(input_file) as f:
        content = f.readlines()
    
    res = 0

    content = np.array([list(cont) for cont in content])[:, :-1]
    print(content)

    xs,ys = np.where(content == 'A')
    for x, y in zip(xs, ys):
        res += check_xmas(content, x, y)

    print(res)