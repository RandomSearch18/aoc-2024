from typing import Sequence, Union


def find_smallest(numbers: list[Union[int, None]]) -> int:
    smallest_index = 0
    for current in range(1, len(numbers)):
        if numbers[current] and numbers[current] < numbers[smallest_index]:  # type: ignore
            smallest_index = current
    return smallest_index


def solve(input_rows: list[tuple[int, int]]) -> int:
    left_numbers: list[Union[int, None]] = [row[0] for row in input_rows]
    right_numbers: list[Union[int, None]] = [row[1] for row in input_rows]

    count = 0
    while count < len(left_numbers):
        smallest_left = find_smallest(left_numbers)
        smallest_right = find_smallest(right_numbers)
        distance = abs(left_numbers[smallest_left] - right_numbers[smallest_right])


with open("1/input.txt", "r") as file:
    data = file.read().strip()
    input_rows = []
    for line in data.split("\n"):
        numbers = line.split("   ")
        input_rows.append((int(numbers[0]), int(numbers[1])))
    # print(input_rows)
    solve(input_rows)
