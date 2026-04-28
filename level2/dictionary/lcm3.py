line = input().split()
res = {}
for word in line:
    if len(word) not in res:
        res[len(word)] = 1
    else:
        res[len(word)] += 1
print(res)
