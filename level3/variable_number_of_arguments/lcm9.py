def cactus(*args: list[int]) -> list[int]:
    cactus_list = []
    for num in args:
        num = str(num)
        len_num = len(num)
        first = int(num[0])
        second = int(num[-1])
        if len(num) > 2 and second != 0 and first != 0:
            if int(num[1:-1]) % first != 0 and int(num[1:-1]) % second != 0:
                cactus_list.append(int(num))
    return cactus_list


print(*cactus(73149, 36996, 63321, 25539, 33573, 50508, 84220, 22506, 39793, 300))
