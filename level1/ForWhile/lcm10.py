word = input()
res = ""
for letter in word:
    if letter not in "aeiouyAEIOUY":
        res += letter
print(res)
