def count_safe_rows(reports: list[list[int]]) -> int:
    total_safe_rows = 0
    for report in reports:
        if is_safe(report):
            total_safe_rows += 1
    return total_safe_rows


def count_safe_rows_with_dampener(reports: list[list[int]]) -> int:
    total_safe_rows = 0
    for report in reports:
        if is_safe_with_dampener(report):
            total_safe_rows += 1
    return total_safe_rows


def is_safe(report: list[int]) -> bool:
    direction = 0
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        direction
        if diff < 0:
            if direction == 1:
                return False
            direction = -1
        elif diff > 0:
            if direction == -1:
                return False
            direction = 1
        abs_diff = abs(diff)
        if not (1 <= abs_diff <= 3):
            return False
    return True


def is_safe_with_dampener(report: list[int], allow_a_problem: bool = True) -> bool:
    has_problem = False

    def found_problem(i: int):
        if not allow_a_problem:
            print(f"Found unsafe row: {report}")
            nonlocal has_problem
            has_problem = True
            return False
        report.pop(i)
        return is_safe_with_dampener(report, allow_a_problem=False)

    direction = 0
    # for i in range(1, len(report)):
    i = 1
    while i < len(report):
        diff = report[i] - report[i - 1]
        direction
        if diff < 0:
            if direction == 1:
                return found_problem(i)
            direction = -1
        elif diff > 0:
            if direction == -1:
                return found_problem(i)
            direction = 1
        abs_diff = abs(diff)
        if not (1 <= abs_diff <= 3):
            return found_problem(i)
        i += 1

    if has_problem:
        return False
    print(f"Found safe row: {report}")
    return True


with open("2/input.txt", "r") as file:
    data = file.read().strip()
    input_rows = []
    for line in data.split("\n"):
        report = line.split(" ")
        levels = [int(lvl) for lvl in report]
        input_rows.append(levels)

    # print(count_safe_rows(input_rows))
    print(count_safe_rows_with_dampener(input_rows))
