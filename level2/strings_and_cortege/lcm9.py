num_R = int(input())
line = list("R" * num_R)
i = 0
while i < len(line) - 2:
    if line[i] == line[i + 1] == line[i + 2]:
        new_char = "S" if line[i] == "R" else "R"
        line[i : i + 3] = [new_char]
        i = max(0, i - 2)
    else:
        i += 1
print("".join(line))
