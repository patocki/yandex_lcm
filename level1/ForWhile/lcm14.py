word = input()
length = 0
for letter in word:
    if letter != " ":
        length += 1
    else:
        print(*range(1, length + 1), sep=" ", end=" \n")
        length = 0
print(*range(1, length + 1), sep=" ", end=" \n")
