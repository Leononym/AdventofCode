with open("datainput") as f:
    input_data = list(f.readlines())

valid_passwords = 0

for i in input_data:
    password = str(i).split(" ")[2]
    password_policy = str(i).split(": ")[0]
    position1 = int(str(password_policy).split("-")[0])
    position2 = int(str(password_policy).split("-")[1].split(" ")[0])
    given_letter = str(password_policy).split(" ")[1]
    if password[position1 - 1] == password[position2 - 1]:
        continue
    elif password[position1 - 1] == given_letter or password[position2 - 1] == given_letter:
        valid_passwords += 1

print(valid_passwords)