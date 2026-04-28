line = input()
colors = set()
while line:
    line = line.lower()
    colors.add(line)
    line = input()
for clr in colors:
    print(clr)
