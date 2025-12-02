
import re

def process_data(data, is_valid_cb):
    ranges = data.split(",")
    parser = lambda range: tuple(map(int, range.split("-")))
    parsed = list(map(parser, ranges))
    result = 0
    for id_from, id_to in parsed:
        for id in range(id_from, id_to + 1):
            if not is_valid_cb(str(id)):
                result += id
    return result

def part1(data: str):
    is_valid = lambda id: not re.search(r"^(\d+)\1$", id)
    return process_data(data, is_valid)

def part2(data: str):
    is_valid = lambda id: not re.search(r"^(\d+)\1+$", id)
    return process_data(data, is_valid)
