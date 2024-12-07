import re


pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

def read_input(input_file: str) -> str:
    with open(input_file) as f:
        content = f.readlines()
        content = ''.join(content)
    return content


def level1(instruction: str) -> int:
    matches = re.findall(pattern, instruction)
    res = 0
    for a in matches:
        res += int(a[0])*int(a[1])
    return res

def level2(instruction: str) -> int:
    donts = instruction.split("don't()")

    res = level1(donts.pop(0))

    for dont in donts:
        dos = dont.split('do()')
        if len(dos) > 1 :
            res += level1(' '.join(dos[1:]))
    return res


if __name__ == "__main__":

    input_file = './Day03/input1.txt'
    
    instruction = read_input(input_file=input_file)

    print('level 1 : ', level1(instruction=instruction))
    print('level 2 : ', level2(instruction=instruction))
