def part1(data: str) -> int:
    length, width, height = map(int, data.split("x"))

    side1 = length * width
    side2 = width * height
    side3 = height * length

    return 2 * (side1 + side2 + side3) + min(side1, side2, side3)


def parse_input(path: str) -> None:
    total = 0
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += part1(line)

    print("Part 1:", total)


if __name__ == "__main__":
    data = parse_input("2015/day02/input.txt")
