def part1(data: str):
    raw = data.split("\n\n")
    parser = lambda range: tuple(map(int, range.split("-")))
    ranges = list(map(parser, raw[0].splitlines()))
    ids = list(map(int, raw[1].splitlines()))

    result = 0
    for id in ids:
        for range in ranges:
            if range[0] <= id <= range[1]:
                result += 1
                break

    return result


def part2(data: str):
    raw = data.split("\n\n")
    parser = lambda range: tuple(map(int, range.split("-")))
    ranges = sorted(list(map(parser, raw[0].splitlines())), key=lambda x: x[0])
    result = 0
    last_max = 0
    for r_start, r_end in ranges:
        if last_max > r_end:
            continue
        result += r_end - r_start + 1
        if last_max >= r_start:
            result -= last_max - r_start + 1
        last_max = r_end

    return result
