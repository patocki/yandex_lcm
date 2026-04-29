def important(first: str, second: str, *args):
    return [
        word
        for word in args
        if (first.lower() in word or first.upper() in word)
        and (second.lower() not in word and second.upper() not in word)
    ]
