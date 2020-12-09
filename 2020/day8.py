data = [line.rstrip() for line in open("day8_data")]
i = 0
instructions = []
accumulator = 0

while i not in instructions:
    instructions.append(i)
    if data[i].startswith("nop"):
        i += 1
    if data[i].startswith("acc"):
        accumulator += int(data[i].split(" ")[1])
        i += 1
    if data[i].startswith("jmp"):
        i += int(data[i].split(" ")[1])

print(accumulator)
