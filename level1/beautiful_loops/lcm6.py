first_num = int(input())
rows = int(input())
cols = int(input())

for i in range(rows):
    for j in range(cols):
        if (j + 1) % 2 != 0:
            print(first_num + (j * rows) + i, end="\t")
        else:
            print(first_num + ((j + 1) * rows) - (i + 1), end="\t")
    print()
