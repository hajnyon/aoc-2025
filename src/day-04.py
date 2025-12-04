def get_arr(data):
    lines = data.splitlines()
    empty_arr = [None] * (len(lines) + 2)
    two_d_arr = [[None] + list(row) + [None] for row in lines]
    arr = [empty_arr, *two_d_arr, empty_arr]
    return arr

def solve(arr, replace = False):
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
                if replace:
                    arr[row][col] = "."
                result += 1

    return result

def part1(data: str):
    arr = get_arr(data)
    return solve(arr)

def part2(data: str):
    arr = get_arr(data)

    result = 0
    is_changed = True
    while is_changed:
        is_changed = False
        r = solve(arr, True)
        if r > 0:
            is_changed = True
        result += r

    return result
