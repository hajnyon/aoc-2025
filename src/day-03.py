
def part1(data: str):
    result = 0
    for line in data.splitlines():
        max = 0
        for i in range(len(line)):
            cur = line[i]
            for j in range(i + 1, len(line)):
                num = int(cur + line[j])
                if num > max:
                    max = num
        result += max
    return result

def part2(data: str):
    result = 0
    for line in data.splitlines():
        str = ""
        start_index = 0

        for end_index in range(len(line) - 12 + 1, len(line) + 1):
            max_digit = max(line[start_index:end_index])
            max_digit_index = line[start_index:].index(max_digit)
            start_index += max_digit_index + 1
            str += line[start_index - 1]

        result += int(str)
    return result
