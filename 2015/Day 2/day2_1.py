input_data = []
wrapping_paper = 0
with open("inputdata") as f:
    input_data = list(f.readlines())

for i in input_data:
    l = int(str(i).split("x")[0])
    w = int(str(i).split("x")[1])
    h = int(str(i).split("x")[2].split("\\")[0])
    a = l*w
    b = w*h
    c = h*l
    surface_area = 2*a + 2*b + 2*c + min(a, b, c)
    wrapping_paper += surface_area
print(wrapping_paper)