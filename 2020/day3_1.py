data = []
position = 1
row = 0
trees = 0
with open("day3_data") as f:
    l1 = list(f.readlines())
    for i in l1:
        data.append(i.split("\n")[0])

for i in data:
    if row == len(data) - 1:
        print(trees)
        break

    row += 1
    if position <= 28:
        position += 3
    else:
        position += 3
        position -= 31

    if data[row][position - 1] == "#":
        trees += 1
