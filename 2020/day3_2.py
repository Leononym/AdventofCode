data = []
multiplied_trees = 1
slope_right = [1,3,5,7,1]
slope_down = [1,1,1,1,2]
with open("day3_data") as f:
    l1 = list(f.readlines())
    for i in l1:
        data.append(i.split("\n")[0])

for x in range(5):
    trees = 0
    row = 0
    position = 1
    for i in data:
        if row == len(data) - 1:
            print(f"Right {slope_right[x]}, down {slope_down[x]}: {trees} Trees")
            break

        row += slope_down[x]
        if position <= 31 - slope_right[x]:
            position += slope_right[x]
        else:
            position += slope_right[x]
            position -= 31

        if data[row][position - 1] == "#":
            trees += 1
    multiplied_trees *= trees

print("Multiplied:", multiplied_trees)
