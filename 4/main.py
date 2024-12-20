from enum import Enum
from turtle import down


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
                grid, word[1:], to_check, direction, visited + [start]
            )

    return None


def find_words(
    grid: list[list[str]], word: str, directions: list[Direction]
) -> list[Match]:
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
            if len(word) == 1 and match.start == existing_match.start:
                # Spacial case for when we're looking for a single letter, otherwise it'll return a dupe for every direction
                return True
        return False

    for y in range(height):
        for x in range(width):
            for direction in directions:
                match = find_word_from_pos(grid, word, (y, x), direction)
                if match:
                    # Check for duplicates
                    if not is_already_found(match):
                        found.append(match)

    return found


def find_xmases(grid: list[list[str]]) -> int:
    matches = find_words(
        grid,
        "XMAS",
        list(Direction),
    )
    return len(matches)


def is_x_mas(grid: list[list[str]], start: tuple[int, int]) -> bool:
    # x, y = start
    y, x = start  # not scuffed at all (!)
    if not is_in_bounds(grid, (y + 1, x + 1)):
        return False
    if not is_in_bounds(grid, (y - 1, x - 1)):
        return False
    up_left = grid[y - 1][x - 1]
    up_right = grid[y - 1][x + 1]
    down_left = grid[y + 1][x - 1]
    down_right = grid[y + 1][x + 1]
    diagonal_1 = (up_left == "M" and down_right == "S") or (
        up_left == "S" and down_right == "M"
    )
    diagonal_2 = (up_right == "M" and down_left == "S") or (
        up_right == "S" and down_left == "M"
    )
    return diagonal_1 and diagonal_2


def find_x_mases(grid: list[list[str]]) -> int:
    x_mases = []

    def is_already_found(coords: tuple[int, int]) -> bool:
        for existing in x_mases:
            if coords == existing:
                return True
        return False

    found_a = find_words(grid, "A", list(Direction))
    # print([match.coordinates for match in found_a])
    for a_coords in found_a[0].coordinates:  # ???
        if is_x_mas(grid, a_coords):
            if not is_already_found(a_coords):
                x_mases.append(a_coords)
    print(x_mases)
    return len(x_mases)


with open("4/input.txt", "r") as file:
    data = file.read().strip()
    grid = [list(row) for row in data.split("\n")]
    # print(find_xmases(grid))
    print(find_x_mases(grid))
