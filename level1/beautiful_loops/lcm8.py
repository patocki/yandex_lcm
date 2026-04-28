length = int(input())
for i in range(length + 1):
    for j in range(length + 1 - i):
        if j < length - i:
            print("|", end="\t")
        else:
            print("O")
