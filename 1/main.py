def solve(input_rows: list[tuple[int, int]]) -> int:
    left_numbers = [row[0] for row in input_rows]
    right_numbers = [row[1] for row in input_rows]


with open("1/input.txt", "r") as file:
    data = file.read().strip()
    input_rows = []
    for line in data.split("\n"):
        numbers = line.split("   ")
        input_rows.append((int(numbers[0]), int(numbers[1])))
    # print(input_rows)
    solve(input_rows)
