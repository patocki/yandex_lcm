dict_clrs = {}
while True:
    line = input()
    if line == "ENOUGH":
        break
    dict_clrs[line] = dict_clrs.get(line, 0) + 1
for i, j in sorted(dict_clrs.items()):
    print(f"{i}: {j}")
