num = int(input())
max = 0
min1 = min2 = 205
for i in range(num):
    max = int(input())
    if max < min1:
        min2, min1 = min1, max
    elif max < min2:
        min2 = max
print(min2)
