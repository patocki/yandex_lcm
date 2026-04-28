num = int(input())
state = "Простое"
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        state = "НЕТ"
        break
    elif num // i == 0:
        state = "НЕТ"
        break
if num == 1:
    state = "НЕТ"
print(state)
