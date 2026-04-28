boots = input().split()
num = int(input())
k = 0
for i in range(num):
    print(f"{i + 1}-я пара ножек: {boots[k].lower()}{"." if (i + 1) == num else ";"}")
    if k == len(boots) - 1:
        k = 0
    else:
        k += 1
