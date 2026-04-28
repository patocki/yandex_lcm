delitel = int(input())
dict_nums = {x: [] for x in range(delitel)}
while True:
    num = input()
    if not num:
        break
    dict_nums[int(num) % delitel].append(int(num))
number_query = int(input())
for _ in range(number_query):
    num = int(input())
    if num in dict_nums and len(dict_nums[num]) != 0:
        print(round(sum(dict_nums[num]) / len(dict_nums[num]), 5))
    else:
        print(-1)
