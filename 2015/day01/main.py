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


def part2(data: list[str]) -> None:
    floor: int = 0
    basement = 0

    for i, char in enumerate(data, start=1):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor == -1:
            return i


if __name__ == "__main__":
    data = parse_input("2015/day01/input.txt")
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
