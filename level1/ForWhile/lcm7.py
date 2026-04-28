w = "Светлая полоса"
b = "Тёмная полоса"
num = int(input())
st = int(input())
for i in range(1, num + 1, st):
    print(f"{i}\n{w}")
    w, b = b, w
