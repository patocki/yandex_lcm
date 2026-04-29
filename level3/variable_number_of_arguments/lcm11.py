def ideal(*words):
    candidats = {word: [len(set(word.lower())), len(word), word] for word in words}
    ideal_w = words[0]
    for word in words:
        if word != ideal_w:
            if candidats[word][0] > candidats[ideal_w][0]:
                ideal_w = word
            elif candidats[word][0] == candidats[ideal_w][0]:
                if candidats[word][1] > candidats[ideal_w][1]:
                    ideal_w = word
                elif candidats[word][1] == candidats[ideal_w][1]:
                    if candidats[word][2] > candidats[ideal_w][2]:
                        ideal_w = word
    return ideal_w


print(ideal("Spring", "morning", "Time"))
