min_size = int(input())
num_cuc = int(input())
count_normal = 0
little_flag = False
big_flag = False
for i in range(num_cuc):
    cucumber = int(input())
    if cucumber < min_size:
        little_flag = True
        continue
    elif cucumber > min_size * 2:
        big_flag = True
        continue
    else:
        count_normal += 1

if count_normal != 0:
    print(count_normal)
elif little_flag and not big_flag:
    print("Маленькие ещё.")
elif big_flag and not little_flag:
    print("Переросли!")
else:
    print("Нечего собирать!")
