import re

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'


def mulitply_regex(weird):
    # Find all matches in the text
    matches = re.findall(pattern, weird)
    
    res = 0
    for a in matches:
        res += int(a[0])*int(a[1])
    return res

if __name__ == "__main__":

    # Define the file's name.
    input_file = './Day_3/input_1.txt'

    # Open the file and read its content.
    with open(input_file) as f:
        content = f.readlines()
    

    content = ' '.join(content)

    donts = content.split("don't()")

    res = mulitply_regex(donts.pop(0))
    print(res)

    for dont in donts:
        dos = dont.split('do()')
        if len(dos) > 1 :
            res += mulitply_regex(' '.join(dos[1:]))


    print(res)

