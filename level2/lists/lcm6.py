list_clrs = []
line = input()
while line:
    list_clrs.append(line)
    line = input()
num = int(input())
j = 0
for i in range(num):
    print(f"Мороз {list_clrs[j]} Нос.")
    j += 1
    if j == len(list_clrs):
        j = 0
