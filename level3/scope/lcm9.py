words = []


def learn(word: str):
    if word in words:
        words.insert(words.index(word), word)
    else:
        words.append(word)
