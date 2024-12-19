from enum import Enum


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP_LEFT = (-1, -1)
    UP_RIGHT = (-1, 1)
    DOWN_LEFT = (1, -1)
    DOWN_RIGHT = (1, 1)


def is_in_bounds(grid: list[list[str]], coordinates: tuple[int, int]) -> bool:
    height = len(grid)
    width = len(grid[0])
    y, x = coordinates
    return 0 <= y < height and 0 <= x < width


class Match:
    def __init__(self, coordinates: list[tuple[int, int]], direction: Direction):
        self.start = coordinates[0]
        self.coordinates = coordinates
        self.direction = direction


def find_word_from_pos(
    grid: list[list[str]],
    word: str,
    start: tuple[int, int],
    direction: Direction,
    visited=[],
) -> Match | None:
    y, x = start

    if grid[y][x] == word[0]:
        if len(word) == 1:
            visited.append(start)
            return Match(visited, direction)

        dy, dx = direction.value
        to_check = (y + dy, x + dx)
        if is_in_bounds(grid, to_check):
            return find_word_from_pos(
                grid, word[1:], to_check, direction, visited.extend([start])
            )

    return None


def find_xmases(grid: list[list[str]]) -> int:
    height = len(grid)
    width = len(grid[0])
    found: list[Match] = []

    def is_already_found(match: Match) -> bool:
        for existing_match in found:
            if (
                match.start == existing_match.start
                and match.direction == existing_match.direction
            ):
                return True
        return False

    for y in range(height):
        for x in range(width):
            for direction in Direction:
                match = find_word_from_pos(grid, "XMAS", (y, x), direction)
                if match:
                    # Check for duplicates
                    if not is_already_found(match):
                        found.append(match)

    return len(found)


with open("4/input.txt", "r") as file:
    data = file.read().strip()
    grid = [list(row) for row in data.split("\n")]
    print(find_xmases(grid))
