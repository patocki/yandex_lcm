a = int(input())
b = int(input())
operand = input()
c = int(input())
d = int(input())
if operand == "+":
    up = a * d + b * c
else:
    up = a * d - b * c
down = b * d
i, j = up, down
samedel = 0
while i * j != 0:
    i, j = j, i % j
samedel = i + j
print(f"{up // samedel} / {down // samedel}")
