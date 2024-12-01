def solve() -> int:
    pass


with open("1/input.txt", "r") as file:
    data = file.read().strip()
    input_cols = [line.split("   ") for line in data.split("\n")]
    print(input_cols)
