num = int(input())
base = 12
s = ""
while num > 0:
    if num % base == 10:
        s = "A" + s
    elif num % base == 11:
        s = "B" + s
    elif num % base == 12:
        s = "C" + s
    else:
        s = str(num % base) + s
    num = num // base
print(s)
