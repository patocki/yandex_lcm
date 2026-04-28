word = input()
i = 1
while word[::-1] != word:
    word = word[i:-i]
print(word)
