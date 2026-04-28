word = input()
res = ""
for letter in word:
    if letter == " ":
        print(*res, sep="_")
        res = ""
    else:
        res += letter

print(*res, sep="_")
