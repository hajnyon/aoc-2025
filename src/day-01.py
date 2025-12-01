
mod = 100

def part1(data: str):
    rotations = data.splitlines()
    result = 0
    dial = 50
    for rotation in rotations:
        value = int(rotation[1:])
        if rotation[0] == 'R':
            value = -value
        dial = (dial + value) % mod
        if dial == 0:
            result += 1
    return result

def part2(data: str):
    rotations = data.splitlines()
    result = 0
    dial = 50
    for rotation in rotations:
        value = int(rotation[1:])
        if rotation[0] == 'R':
            value = -value
        dial_change = dial + value
        new_dial = dial_change % mod

        result += abs(dial_change // mod)
        if dial_change <= 0:
            if new_dial == 0:
                # add 1 if landing directly on 0
                result += 1
            if dial == 0:
                # correct count when starting on 0 and moving to negative
                result -= 1

        dial = new_dial

    return result
