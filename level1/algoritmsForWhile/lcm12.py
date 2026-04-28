num = int(input())
sc = 0
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        if i % 2 == 0:
            sc += 1
        if num // i != i and (num // i) % 2 == 0:
            sc += 1
print(sc)
