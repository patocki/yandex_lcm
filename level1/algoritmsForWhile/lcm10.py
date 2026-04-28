num = int(input())
base = 7
s = ""
i = 0
while num > 0:
    s = str(num % base) + s
    if int(num % base) == 6:
        i += 1
    num //= base

print(i)
