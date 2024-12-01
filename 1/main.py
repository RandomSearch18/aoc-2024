def solve(input_cols: list[tuple[int, int]]) -> int:
    pass


with open("1/input.txt", "r") as file:
    data = file.read().strip()
    input_cols = []
    for line in data.split("\n"):
        numbers = line.split("   ")
        input_cols.append((int(numbers[0]), int(numbers[1])))
    print(input_cols)
