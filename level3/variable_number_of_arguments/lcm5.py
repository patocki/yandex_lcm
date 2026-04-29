def builder(num: int, *words):
    return "".join([word[num] for word in words])
