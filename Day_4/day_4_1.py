import numpy as np


def count_xmas_occurrences(text):
    # Convert text to uppercase to make the search case-insensitive
    text_upper = text.upper()
    
    # Count forward occurrences
    forward_count = text_upper.count('XMAS')
    
    # Count backward occurrences (reverse the string and search)
    backward_count = text_upper[::-1].count('XMAS')
    
    # return {
    #     'forward': forward_count,
    #     'backward': backward_count,
    #     'total': forward_count + backward_count
    # }
    return forward_count + backward_count


if __name__ == "__main__":

    # Define the file's name.
    input_file = './Day_4/input_1.txt'

    # Open the file and read its content.
    with open(input_file) as f:
        content = f.readlines()
    
    res = 0

    content = np.array([list(cont) for cont in content])[:, :-1]

    for a in content:
        res += count_xmas_occurrences(''.join(a))

    for a in content.T:
        res += count_xmas_occurrences(''.join(a))

    
    for i in range(-content.shape[0], content.shape[1]):
        res += count_xmas_occurrences(''.join(content.diagonal(i)))

    for i in range(-content.shape[1], content.shape[0]):
        res += count_xmas_occurrences(''.join(content.T.diagonal(i)))

    print(res)