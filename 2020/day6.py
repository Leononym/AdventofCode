import string

data = []
temp_data = []

with open("day6_data") as f:
    for line in f.readlines():
        if str(line) == "\n":
            data.append(temp_data)
            temp_data = []
        else:
            temp_data.append(line.rstrip())
    data.append(temp_data)


def part_one():
    total_yes = 0
    for group in data:
        used_letters = ""
        for person in group:
            for question in person:
                if question not in used_letters:
                    used_letters += str(question)
        total_yes += len(used_letters)
    return total_yes


def part_two():
    used_letters = 0
    for group in data:
        str_group = str(group)
        for letter in string.ascii_lowercase:
            if str_group.count(letter) == len(group):
                used_letters += 1
    return used_letters


print(f"Total 'yes'-answers: {part_one()}\n"
      f"Total answers to which everyone in group answered 'yes': {part_two()}")
