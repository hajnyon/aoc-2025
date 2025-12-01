#!/usr/bin/env python3
import sys
from pathlib import Path
import importlib.util

def load_day_module(day_str):
    path = Path(f"src/day-{day_str}.py")
    if not path.exists():
        raise FileNotFoundError(f"Day file not found: {path}")

    spec = importlib.util.spec_from_file_location(f"day_{day_str}", path)
    if not spec:
        raise ImportError(f"Failed to create spec for day {day_str}")
    module = importlib.util.module_from_spec(spec)
    if not module or not spec.loader:
        raise ImportError(f"Failed to create module for day {day_str}")
    spec.loader.exec_module(module)
    return module

def load_input(day_str, is_base=False):

    if is_base:
        base = Path(f"input/day-{day_str}-base.txt")
        if base.exists():
            return base.read_text().rstrip("\n")
        else:
            raise FileNotFoundError(f"No input file found for day {day_str}")

    primary = Path(f"input/day-{day_str}.txt")
    if primary.exists():
        return primary.read_text().rstrip("\n")
    else:
        raise FileNotFoundError(f"No input file found for day {day_str}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_day.py <day-number> [--base]")
        sys.exit(1)

    day = int(sys.argv[1])
    day_str = f"{day:02d}"

    is_base = len(sys.argv) > 2 and (sys.argv[2] == "-b" or sys.argv[2] == "--base")

    module = load_day_module(day_str)
    data = load_input(day_str, is_base)

    part1 = getattr(module, "part1", None)
    part2 = getattr(module, "part2", None)

    if callable(part1):
        print("Part 1:", part1(data))
    else:
        print("Part 1: MISSING")

    if callable(part2):
        print("Part 2:", part2(data))
    else:
        print("Part 2: MISSING")

if __name__ == "__main__":
    main()
