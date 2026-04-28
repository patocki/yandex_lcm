size_field = int(input())
field = []

for k in range(size_field):
    part = []
    for j in range(size_field):
        part.append(".")
    field.append(part)
num_hops = int(input())
turn = 1
for i in range(num_hops):
    coord = list(map(int, input().split()))
    if ((size_field - 1) >= coord[0] >= 0) and ((size_field - 1) >= coord[1] >= 0):
        if turn % 2 != 0 and field[coord[0]][coord[1]] == ".":
            field[coord[0]][coord[1]] = "X"
            for s in range(size_field):
                print(*field[s], sep=" ")
            turn += 1
        elif turn % 2 == 0 and field[coord[0]][coord[1]] == ".":
            field[coord[0]][coord[1]] = "0"
            for s in range(size_field):
                print(*field[s], sep=" ")
            turn += 1
        else:
            print(None)
    else:
        print(None)
