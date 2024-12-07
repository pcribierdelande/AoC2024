import numpy as np

def read_input(input_file: str) -> np.ndarray[str]:
    with open(input_file) as f:
        content = f.readlines()
    return np.array([list(cont) for cont in content])[:, :-1]


def count_xmas_occurrences(text: str) -> int:
    
    # Count forward occurrences
    forward_count = text.count('XMAS')
    
    # Count backward occurrences (reverse the string and search)
    backward_count = text[::-1].count('XMAS')
    
    return forward_count + backward_count


def level1(char_grid: np.ndarray[str]) -> int:
    res = 0

    for a in char_grid:
        res += count_xmas_occurrences(''.join(a))

    for a in char_grid.T:
        res += count_xmas_occurrences(''.join(a))

    for i in range(-char_grid.shape[0], char_grid.shape[1]):
        res += count_xmas_occurrences(''.join(char_grid.diagonal(i)))

    for i in range(-char_grid.shape[1], char_grid.shape[0]):
        res += count_xmas_occurrences(''.join(char_grid.T.diagonal(i)))

    return res


def check_Xmas(char_grid: np.ndarray[str], i: int, j: int) -> bool:
    if i==0 or j==0 or i==char_grid.shape[0]-1 or j==char_grid.shape[1]-1:
        return 0
    search = {'M', 'S'}
    one = {char_grid[i-1,j-1], char_grid[i+1,j+1]}
    two = {char_grid[i-1,j+1], char_grid[i+1,j-1]}
    return one == search and two == search


def level2(char_grid: np.ndarray[str]) -> int:
    res = 0
    xs,ys = np.where(char_grid == 'A')
    for x, y in zip(xs, ys):
        res += check_Xmas(char_grid, x, y)
    return res

if __name__ == "__main__":

    input_file = './Day04/input1.txt'

    char_grid = read_input(input_file)

    print('level 1 : ', level1(char_grid=char_grid))
    print('level 2 : ', level2(char_grid=char_grid))

    
