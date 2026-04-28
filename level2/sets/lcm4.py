line = input().split()
letters = "".join(line).lower()
unic_letters = set(letters)
print(len(unic_letters))
