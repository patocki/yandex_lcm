def multiplier(*args):
    res = 1
    not_null = [arg for arg in args if arg != 0]
    if not_null:
        for num in not_null:
            res *= num
        return res
    return
