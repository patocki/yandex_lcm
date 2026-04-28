list_num = []
num = int(input())
while num != -1:
    list_num.append(num)
    num = int(input())
i = 0
count_chet = 0
count_nechet = 0
while i < len(list_num):
    if list_num[i] % 2 == 0:
        count_chet += 1
    else:
        count_nechet += 1
    i += 1
    if i == len(list_num) and count_chet == count_nechet:
        del list_num[-1]
        count_chet = 0
        count_nechet = 0
        i = 0
if count_chet > count_nechet:
    for i in range(len(list_num)):
        if list_num[i] % 2 != 0:
            list_num[i] -= 1
else:
    for i in range(len(list_num)):
        if list_num[i] % 2 == 0:
            list_num[i] += 1
print(list_num)
