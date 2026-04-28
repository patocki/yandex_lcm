num = int(input())
schet = min = 0
temp = 20
for i in range(num):
    min = int(input())
    if min < temp:
        temp, schet = min, 1
    elif min == temp:
        schet += 1
print(schet)
