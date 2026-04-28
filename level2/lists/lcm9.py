word = input()
words = [word]
orderFL = 0
i = 0
while True:
    word = input()
    if not word:
        print("DONE!")
        break
    words.append(word)
    
    if words[0] < words[1]:
        orderFL = 0
    else:
        orderFL = 1
    if words[i] > words[i + 1] and orderFL == 0:
        print(word)
        break
    elif words[i] < words[i + 1] and orderFL == 1:
        print(word)
        break
    else:
        i += 1
