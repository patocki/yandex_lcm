first_num = int(input())
rows = int(input())
cols = int(input())
for i in range(rows):
    for j in range(cols):
        print(j * rows + first_num + i, end="\t")
    print()
