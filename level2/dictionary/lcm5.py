num = int(input())
dict_heros = {}
for _ in range(num):
    lst = input().split("\t")
    dict_heros[lst[0]] = lst[1]
num2 = int(input())
for _ in range(num2):
    tail = input()
    if tail in dict_heros:
        print(dict_heros[tail])
    else:
        print("KeyError")
