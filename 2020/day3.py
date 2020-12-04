data = []

# read data from file and creates a list from the lines
with open("day3_data") as f:
    l1 = f.readlines()
    for i in l1:
        data.append(i.split("\n")[0])

multiplied_trees = 1
right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]

for x in range(len(right)):
    trees = 0
    row = 0
    position = 1
    for i in data:
        # breaks when the bottom of the map is reached and prints the summery of each loop
        if row == len(data) - 1:
            print(f"Right {right[x]}, down {down[x]}: {trees} Trees")
            break
        # moves position
        row += down[x]
        if position <= 31 - right[x]:
            position += right[x]
        else:
            position += right[x]
            position -= 31

        # detects the trees
        if data[row][position - 1] == "#":
            trees += 1
    multiplied_trees *= trees

print("Multiplied:", multiplied_trees)
