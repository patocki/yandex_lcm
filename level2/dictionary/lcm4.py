line = input()
count_let = {}
for let in line:
    if let not in count_let:
        count_let[let] = 1
    else:
        count_let[let] += 1
    print(count_let[let], end=" ")
