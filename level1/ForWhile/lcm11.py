word = input()
temp = ""
res = ""
for letter in word:
    if temp <= letter and temp != "":
        res += letter
    temp = letter
print(res)
