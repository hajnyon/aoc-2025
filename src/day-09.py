import itertools

def part1(data: str):
    points = list(map(lambda line: tuple(map(int, line.split(','))), data.splitlines()))
    rects = []
    for a, b in itertools.combinations(points, 2):
        sq = abs(a[0] - b[0] + 1) * abs(a[1] - b[1] + 1)
        rects.append(sq)
    return sorted(rects)[-1]


def part2(data: str):
    # TODO: implement
    return None
