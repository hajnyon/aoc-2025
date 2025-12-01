#!/usr/bin/env python3
import os
import sys
from pathlib import Path

DAY_TEMPLATE = """def part1(data: str):
    # TODO: implement
    return None


def part2(data: str):
    # TODO: implement
    return None
"""

def main():
    if len(sys.argv) < 2:
        print("Usage: python new.py <day-number>")
        sys.exit(1)

    day = int(sys.argv[1])
    day_str = f"{day:02d}"

    src_file = Path(f"src/day-{day_str}.py")
    input_dir = Path("input")
    input_file = input_dir / f"day-{day_str}.txt"
    input_base = input_dir / f"day-{day_str}-base.txt"

    # Create folders
    src_file.parent.mkdir(parents=True, exist_ok=True)
    input_dir.mkdir(parents=True, exist_ok=True)

    # Write boilerplate
    if not src_file.exists():
        src_file.write_text(DAY_TEMPLATE.format(day=day_str))
        print(f"Created {src_file}")
    else:
        print(f"{src_file} already exists")

    # Create empty input files
    for f in [input_file, input_base]:
        if not f.exists():
            f.write_text("")
            print(f"Created {f}")
        else:
            print(f"{f} already exists")

if __name__ == "__main__":
    main()
