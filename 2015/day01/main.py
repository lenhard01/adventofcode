def parse_input(path: str) -> list:
    with open(path) as f:
        return f.read().strip()


def part1(data: list[str]) -> int:
    floor: int = 0

    for char in data:
        if char == "(":
            floor += 1
        else:
            floor -= 1
    return floor


def part2(data):
    pass


if __name__ == "__main__":
    data = parse_input("2015/day01/input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
