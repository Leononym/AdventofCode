data = []
temp_data = {}

# read and prepare data as dictionary
with open("day4_data") as f:
    for line in f.readlines():
        if line == "\n":
            data.append(temp_data)
            temp_data = {}
        else:
            temp_data[line.rstrip("\n").split(":")[0]] = line.rstrip("\n").split(":")[1]
    data.append(temp_data)

valid_passports = 0

# validates the categories for part 2
def category_validation(passport):
    if 1920 <= int(passport["byr"]) <= 2002: # birth year between 1920 and 2002
        if 2010 <= int(passport["iyr"]) <= 2020: # issue year between 2010 and 2020
            if 2020 <= int(passport["eyr"]) <= 2030: # expiration year between 2020 and 2030
                if passport["hcl"].startswith("#") and len(passport["hcl"]) == 7: # checks if hair color formatting is valid
                    if passport["ecl"] in "amb, blu, brn, gry, grn, hzl, oth": # checks for eye color
                        if len(passport["pid"]) == 9: # checks for valid passport ID
                            if passport["hgt"].endswith("cm"): # checks if cm or in
                                if 150 <= int(passport["hgt"].rstrip("cm")) <= 193:
                                    return True
                            elif passport["hgt"].endswith("in"):
                                if 59 <= int(passport["hgt"].rstrip("in")) <= 76:
                                    return True

# detects required fields and checks category
for passport in data:
    try:
        if passport["cid"]:
            if len(passport) == 8:
                if category_validation(passport):
                    valid_passports += 1
    except KeyError:
        if len(passport) == 7:
            if category_validation(passport):
                valid_passports += 1

print(f"Invalid: {len(data) - valid_passports}; Valid: {valid_passports}; Total: {len(data)}")
