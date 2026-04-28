num = int(input())
this_set = set(input().split())
next_set = set()
union_set = set()
for i in range(num - 1):
    line = input()
    next_set = set(line.split())
    union_set = next_set & this_set
    result = list(union_set)
    result.sort()
    print(*result)
    this_set = next_set
