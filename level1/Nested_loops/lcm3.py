line = input()
offset = int(input())
result = ""
for letter in line:
    result += chr((ord(letter) - offset - ord("a")) % 26 + ord("a"))
# offset -= 1
print(result)
