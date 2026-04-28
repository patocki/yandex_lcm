res = {}
for i in range(int(input())):
    line = input()
    res[line[-1:]] = line
print(res)
