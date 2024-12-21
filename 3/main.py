# https://regex101.com/r/3Pwth1/1
import re


regex = r"mul\((\d{1,3}),(\d{1,3})\)"

with open("3/input.txt", "r") as file:
    data = file.read().strip()
    matches = re.finditer(regex, data, re.MULTILINE)
    for match in matches:
        print(match.group(1), match.group(2))
