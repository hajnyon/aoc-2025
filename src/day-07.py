import re

def part1(data: str):
    lines = data.splitlines()
    start_line = lines.pop(0)
    cur_beams = [False] * len(start_line)
    cur_beams[start_line.find("S")] = True
    result = 0
    for line in lines:
        splitters = [m.start() for m in re.finditer(r"\^", line)]
        for splitter in splitters:
            if cur_beams[splitter] is False:
                continue
            else:
                cur_beams[splitter] = False
                cur_beams[splitter-1] = True
                cur_beams[splitter+1] = True
                result += 1
    return result

def part2(data: str):
    lines = data.splitlines()
    start_line = lines.pop(0)

    mem = {}

    def solve(row, beam):
        if row == len(lines):
            return 1
        key = f"{row},{beam}"
        if key in mem:
            return mem[key]
        if lines[row][beam] == "^":
            res = solve(row+1, beam-1) + solve(row+1, beam+1)
        else:
            res = solve(row+1, beam)
        mem[key] = res
        return res

    return solve(0, start_line.find("S"))
