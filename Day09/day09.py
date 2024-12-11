def read_input(input_file: str) -> str:
    with open(input_file) as f:
        content = f.readlines()
    return content[0]


def create_dic_disk_files(disk_files: str) -> dict[int, int]:
    return {a: int(c) for a, c in enumerate(disk_files)}


def move_file_by_parts(disk_files: dict[int, int], free_spaces: list[int]) -> list[int]:
    hard_drive_res = [0] * int(disk_files[0])
    i = 1

    free_space = free_spaces.pop(0)
    for a in range(len(disk_files) - 1, 1, -1):
        if i >= a:
            break
        reste_a_remplir = disk_files[a]
        while reste_a_remplir > 0:
            if free_space >= reste_a_remplir:
                hard_drive_res += [a] * reste_a_remplir
                free_space -= reste_a_remplir
                reste_a_remplir = 0
            else:
                hard_drive_res += [a] * free_space
                reste_a_remplir -= free_space
                free_space = free_spaces.pop(0)
                if i == a:
                    hard_drive_res += [i] * reste_a_remplir
                    reste_a_remplir = 0
                else:
                    hard_drive_res += [i] * disk_files[i]

                i += 1
    return hard_drive_res


def create_dic_empty_spaces(
    disk_files: dict[int, int], free_spaces: list[int]
) -> dict[int:int]:
    dic_empty_space = {}
    current = 0
    for idx, (file, free) in enumerate(zip(disk_files.values(), free_spaces)):
        current += file
        dic_empty_space[idx] = current
        current += free
    return dic_empty_space


def build_res(
    disk_files: dict[int, int],
    removed_files: dict[int, int],
    dic_mvt: dict[int, int],
    empty_or: list[int],
) -> list[int]:
    res = []
    for idx, e in enumerate(empty_or):
        if idx in disk_files:
            res += [idx] * disk_files[idx]
        else:
            res += [0] * removed_files[idx]
        res += [0] * e
    for k, v in dic_mvt.items():
        res[k] = v
    return res


def move_entire_file(disk_files: dict[int, int], free_spaces: list[int]) -> list[int]:
    free_spaces_or = free_spaces.copy()
    dic_empty_space = create_dic_empty_spaces(disk_files, free_spaces)
    dic_mvt = {}
    to_remove = []
    for a in range(len(disk_files) - 1, 1, -1):
        file_size = disk_files[a]
        first_free_space = next(
            (i for i, x in enumerate(free_spaces) if x >= file_size), -1
        )
        if first_free_space != -1 and first_free_space < a:
            for i in range(file_size):
                dic_mvt[dic_empty_space[first_free_space] + i] = a
                free_spaces[first_free_space] -= 1
            dic_empty_space[first_free_space] += file_size
            to_remove.append(a)

    disk_result = {}
    removed_files = {}
    for k, v in disk_files.items():
        if k in to_remove:
            removed_files[k] = v
        else:
            disk_result[k] = v

    return build_res(disk_result, removed_files, dic_mvt, free_spaces_or)


def compute_checksum(disk_res: list[int]) -> int:
    return sum(x * y for x, y in zip(disk_res, list(range(len(disk_res)))))


def level1(line: str) -> int:
    disk_files = line[::2]
    free_spaces = [int(a) for a in line[1::2]]
    disck_files_dict = create_dic_disk_files(disk_files)
    return compute_checksum(move_file_by_parts(disck_files_dict, free_spaces))


def level2(line: str) -> int:
    disk_files = line[::2]
    free_spaces = [int(a) for a in line[1::2]]
    disck_files_dict = create_dic_disk_files(disk_files)

    return compute_checksum(move_entire_file(disck_files_dict, free_spaces))


def main():
    input_file = "./Day09/input1.txt"

    line = read_input(input_file)

    print("level 1 : ", level1(line))
    print("level 2 : ", level2(line))


if __name__ == "__main__":
    main()
