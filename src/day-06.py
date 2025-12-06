def part1(data: str):
    lines = data.splitlines()
    operators = lines.pop().split()
    numbers = [list(map(int, line.split())) for line in lines]
    acc = list(map(lambda x: 0 if x == '+' else 1, operators))
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            is_sum = operators[j] == '+'
            if is_sum:
                acc[j] += numbers[i][j]
            else:
                acc[j] *= numbers[i][j]

    return sum(acc)


def part2(data: str):
    lines = data.splitlines()
    operators = lines.pop()
    result, cur_op, col_width = 0, None, 1 # last op has no spacer
    for pos in range(len(operators)-1, -1, -1):
        if operators[pos] == ' ':
            col_width += 1
            continue
        is_sum = operators[pos] == '+'
        res = 0 if is_sum else 1
        for i in range(pos + col_width - 1, pos - 1, -1):
            num = ""
            for j in range(len(lines)):
                num += lines[j][i]
            res = res + int(num) if is_sum else res * int(num)
        result += res
        col_width = 0

    return result
