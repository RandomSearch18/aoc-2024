from typing import Sequence, Union


def find_smallest(numbers: list[Union[int, None]]) -> int:
    smallest_index = -1
    for current in range(1, len(numbers)):
        if numbers[current] is None:
            # Ignore any values that are None
            continue
        if smallest_index == -1:
            # This is the first non-None item we've seen
            smallest_index = current
            continue
        if numbers[current] < numbers[smallest_index]:  # type: ignore
            # The "normal" case where we find a new smallest number
            smallest_index = current
    return smallest_index


def solve(input_rows: list[tuple[int, int]]) -> int:
    total_distance = 0

    left_numbers: list[Union[int, None]] = [row[0] for row in input_rows]
    right_numbers: list[Union[int, None]] = [row[1] for row in input_rows]

    count = 0
    while count < len(left_numbers) - 1:
        smallest_left = find_smallest(left_numbers)
        smallest_right = find_smallest(right_numbers)
        distance = abs(left_numbers[smallest_left] - right_numbers[smallest_right])  # type: ignore
        total_distance += distance
        print(
            f"Matched {left_numbers[smallest_left]} with {right_numbers[smallest_right]} to get {distance}"
        )
        left_numbers[smallest_left] = None
        right_numbers[smallest_right] = None
        count += 1

    return total_distance


with open("1/input.txt", "r") as file:
    data = file.read().strip()
    input_rows = []
    for line in data.split("\n"):
        numbers = line.split("   ")
        input_rows.append((int(numbers[0]), int(numbers[1])))
    # print(input_rows)
    print(solve(input_rows))
