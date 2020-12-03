with open("day1_data") as f:
    data = list(map(int, f.readlines()))

for i in data:
    for j in data:
        if i + j == 2020:
            print(i*j)
