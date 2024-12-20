with open("5/input.txt", "r") as file:
    file_raw = file.read().strip()
    rules_raw, updates_raw = file_raw.split("\n\n")
    rules = [(int(rule[0]), int(rule[1])) for rule in rules_raw.split("|")]
    updates = [
        [int(page) for page in update.split(",")] for update in updates_raw.split("\n")
    ]

    print(rules, updates)
