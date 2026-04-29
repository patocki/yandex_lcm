def ten_sum(arr):
    for i in range(len(arr) - 2):
        if (arr[i] + arr[i + 1] + arr[i + 2]) == 10:
            return i

    return -1


# arr = [2, 4, 9, 0, 1, 3, 6]
# print(ten_sum(arr))
