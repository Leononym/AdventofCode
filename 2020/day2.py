import re

with open("day2_data") as f:
    input_data = f.readlines()

valid_passwordsPart1 = 0
valid_passwordsPart2 = 0
pattern = "([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)"

for i in input_data:
    # gets data into single variables
    match = re.match(pattern, i)
    letter_count = 0
    password = match.group(4)
    min_number = int(match.group(1))
    max_number = int(match.group(2))
    given_letter = match.group(3)
    # Part 1
    if min_number <= password.count(given_letter) <= max_number:
        valid_passwordsPart1 += 1
    # Part 2
    if password[min_number - 1] == password[max_number - 1]:
        continue
    elif password[min_number - 1] == given_letter or password[max_number - 1] == given_letter:
        valid_passwordsPart2 += 1

print(f"Valid passwords Part 1: {valid_passwordsPart1}\nValid passwords Part 2: {valid_passwordsPart2}")
