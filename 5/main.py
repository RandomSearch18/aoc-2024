def find_pages_that_should_be_after(rules, page: int):
    result_pages = []
    for rule in rules:
        before, after = rule
        if page == before:
            result_pages.append(after)
    return result_pages


def find_pages_that_should_be_before(rules, page: int):
    result_pages = []
    for rule in rules:
        before, after = rule
        if page == after:
            result_pages.append(before)
    return result_pages


def update_is_correct(rules, update):
    for i, page in enumerate(update):
        for before in find_pages_that_should_be_before(rules, page):
            if before in update:
                # Check if the page comes before the current item
                if not before in update[:i]:
                    # print(f"{before} does not come before {page} in {update}")
                    return False
        for after in find_pages_that_should_be_after(rules, page):
            if after in update:
                # Check if the page comes after the current item
                if not after in update[i:]:
                    # print(f"{after} does not come after {page} in {update}")
                    return False
    return True


with open("5/input.txt", "r") as file:
    file_raw = file.read().strip()
    rules_raw, updates_raw = file_raw.split("\n\n")
    rules = [
        (int(rule.split("|")[0]), int(rule.split("|")[1]))
        for rule in rules_raw.split("\n")
    ]
    updates = [
        [int(page) for page in update.split(",")] for update in updates_raw.split("\n")
    ]

    # print(rules, updates)
    sum_of_middle_page_numbers = 0
    incorrect_updates = []
    for update in updates:
        # print(update, update_is_correct(rules, update))
        if update_is_correct(rules, update):
            sum_of_middle_page_numbers += update[len(update) // 2]
        else:
            incorrect_updates.append(update)
    print(sum_of_middle_page_numbers)
