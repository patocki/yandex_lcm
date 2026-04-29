n = 10


def countdown():
    global n
    result = n
    if n > 0:
        n -= 1
        return result
    else:
        return "START"
