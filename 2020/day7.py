import string

final_data = {}
data = [line.rstrip() for line in open("day7_data")]
for i in data:
    final_data[i.split(" contain")[0]] = 0

for i in final_data:
    for j in data:
        lists = []
        if j.startswith(i):
            j = list(j.split("contain ")[1].split(".")[0].split(", "))
            for k in j:
                if k.endswith("s"):
                    lists.append(k[2:])
                else:
                    lists.append(k[2:] + "s")
            final_data[i] = lists

def part_one():
    can_contain_shiny_gold = ["shiny gold bags"]
    remove = []

    while True:
        old = len(remove)
        for j in final_data:
            for k in can_contain_shiny_gold:
                if k in final_data[j]:
                    can_contain_shiny_gold.append(j)
                    remove.append(j)

        if old == len(remove):
            break
        for h in remove:
            try:
                final_data.pop(str(h))
            except KeyError:
                pass

    final_contains = []
    for i in can_contain_shiny_gold:
        if not i in final_contains:
            final_contains.append(i)
    return len(final_contains) - 1

def part_two():
    contained_by_shiny_gold = []

    while True:
        for i in final_data:


print(f"Number of bags which could contain a shiny gold bag: {part_one()}")
