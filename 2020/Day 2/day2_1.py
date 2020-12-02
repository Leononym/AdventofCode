with open("datainput") as f:
    input_data = list(f.readlines())

valid_passwords = 0

for i in input_data:
    letter_count = 0
    password = str(i).split(" ")[2]
    password_policy = str(i).split(": ")[0]
    min_number = int(str(password_policy).split("-")[0])
    max_number = int(str(password_policy).split("-")[1].split(" ")[0])
    given_letter = str(password_policy).split(" ")[1]
    for letter in password:
        if letter == given_letter:
            letter_count += 1
    if min_number <= letter_count and letter_count <= max_number:
        valid_passwords += 1

print(valid_passwords)