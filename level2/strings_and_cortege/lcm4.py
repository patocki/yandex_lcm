text = input()
first_mismatch = 0
for i in range(0, len(text)):
    if text[i] != text[-(i + 1)]:
        first_mismatch = i
        break
print(first_mismatch)
