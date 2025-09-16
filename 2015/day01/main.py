def parse_input(path: str) -> list:
    with open(path) as f:
        return [line.strip() for line in f]
