first_num = int(input())
cols = int(input())
rows = first_num // cols

for i in range(rows):
    for j in range(cols):
        if (i + 1) % 2 != 0:
            print(first_num - (i  * cols) - j, end="\t")
        else:
            
            print(first_num - ((i+1) * cols) + j + 1, end="\t")
    print()
