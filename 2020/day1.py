with open("day1_data") as f:
    data = list(map(int, f.readlines()))

def part1(data):
    for i in data:
        for j in data:
            if i + j == 2020:
                return i * j

def part2(data):
    for i in data:
        for j in data:
            for k in data:
                if i + j + k == 2020:
                    return i*j*k

print(f"Part 1: {part1(data)}\nPart 2: {part2(data)}")