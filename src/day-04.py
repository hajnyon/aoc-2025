def part1(data: str):
    lines = data.splitlines()
    empty_arr = [None] * (len(lines) + 2)
    two_d_arr = [[None] + list(row) + [None] for row in lines]
    arr = [empty_arr, *two_d_arr, empty_arr]

    result = 0
    for row in range(1, len(arr) - 1):
        for col in range(1, len(arr[row]) - 1):
            if arr[row][col] is None or arr[row][col] == ".":
                continue
            cnt = 0
            for direction in [(0, 1), (0, -1), (1, -1), (1, 0), (1, 1), (-1, 0), (-1, -1), (-1, 1)]:
                if arr[row + direction[0]][col + direction[1]] == "@":
                    cnt += 1
            if cnt < 4:
                result += 1

    return result


def part2(data: str):
    lines = data.splitlines()
    empty_arr = [None] * (len(lines) + 2)
    two_d_arr = [[None] + list(row) + [None] for row in lines]
    arr = [empty_arr, *two_d_arr, empty_arr]

    result = 0
    is_changed = True
    while is_changed:
        is_changed = False
        for row in range(1, len(arr) - 1):
            for col in range(1, len(arr[row]) - 1):
                if arr[row][col] is None or arr[row][col] == ".":
                    continue
                cnt = 0
                for direction in [(0, 1), (0, -1), (1, -1), (1, 0), (1, 1), (-1, 0), (-1, -1), (-1, 1)]:
                    if arr[row + direction[0]][col + direction[1]] == "@":
                        cnt += 1
                if cnt < 4:
                    is_changed = True
                    arr[row][col] = "."
                    result += 1

    return result
