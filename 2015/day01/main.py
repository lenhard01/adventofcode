def parse_input(path: str) -> list:
    with open(path) as f:
        return [line.strip() for line in f]


def part1(data):
    pass


def part2(data):
    pass


if __name__ == "__main__":
    data = parse_input("input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
