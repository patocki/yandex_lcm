numbers = input().split()
res = []
for n in numbers:
    res.append(int(n))
for i in range(len(res) - 1):
    if res[i + 1] > res[i]:
        print(i)
        break
    if i == len(res) - 2:
        print(-1)
