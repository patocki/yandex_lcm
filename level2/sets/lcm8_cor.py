num = int(input())
result_set = set()
for i in range(num):
    line = input()
    set_let = set(line)
    if len(line) == len(set_let):
        result_set.add(line)
print(result_set)
