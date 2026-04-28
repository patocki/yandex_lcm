num = int(input())
nums = []
while -1000 < num < 1000:
    nums.append(num)
    num = int(input())
extremum = input()
if extremum == "max":
    max_num = max(nums)
    print(nums.index(max_num), max_num)
else:
    min_num = min(nums)
    print(nums.index(min_num), min_num)
