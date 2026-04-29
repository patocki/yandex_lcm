def coins(req_sum: int, arr: list[int]) -> list[int]:
    arr_coins = []
    count_arr = {}
    arr.sort(reverse=True)
    temp_sum = req_sum
    for num in arr:
        count_arr[num] = temp_sum // num
        temp_sum = temp_sum % num
    for i, k in count_arr.items():
        arr_coins.extend([i for _ in range(k)])
    return arr_coins


# money = [2, 1, 3]
# print(coins(13, money))
