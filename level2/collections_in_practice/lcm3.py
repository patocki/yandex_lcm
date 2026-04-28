num = int(input())
river_to_sea = {}
for _ in range(num):
    river, sea = input().split(" - ")
    river_to_sea[sea] = river_to_sea.get(sea, []) + [river]
num_request = int(input())
for _ in range(num_request):
    sea = input()
    ans = river_to_sea[sea]
    ans.sort()
    print(", ".join(ans))
