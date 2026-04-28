num = int(input())
s = ""
for i in range(2, num):
    while num % i == 0:
        if s == "":
            s = str(i)
        else:
            s += "*" + str(i)
        num //= i
print(s)
