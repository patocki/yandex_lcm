start = int(input())
end = int(input())
a = int(start**0.5)
if float(a) < start**0.5:
    a += 1
for i in range(a, int(end**0.5) + 1):
    print(i * i, end=" ")
