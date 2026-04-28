num = int(input())
f1 = f2 = 1
sum = 0
prevsum = sum
while sum <= num:
    prevsum = sum
    sum = f1 + f2
    f1, f2 = f2, f1 + f2

print(prevsum)
