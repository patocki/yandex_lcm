def three_divisors(num):
    divisors_list = []
    for i in range(1, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            divisors_list.append(i)
            if i != num // i:
                divisors_list.append(num // i)
    divisors_list.sort()
    len_list = len(divisors_list)
    if len_list == 2:
        second = None
        third = divisors_list[len_list - 2]
    else:
        second = divisors_list[len_list - 2]
        third = divisors_list[len_list - 3]
    first = num
    return (first, second, third)
