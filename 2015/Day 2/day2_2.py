input_data = []
ribbon_total = 0
with open("inputdata") as f:
    input_data = list(f.readlines())

for i in input_data:
    l = int(str(i).split("x")[0])
    w = int(str(i).split("x")[1])
    h = int(str(i).split("x")[2].split("\\")[0])
    a = min(l, w, h)
    c = max(l, w, h)
    if a == l:
        if c == w:
            b = h
        else:
            b = w
    elif a == w:
        if c == l:
            b = h
        else:
            b = l
    else:
        if c == l:
            b = w
        else:
            b = l
    ribbon_total += 2*a + 2*b + l*w*h

print(ribbon_total)