def count_vowels(line):
    line = line.replace(" ", "").lower()
    num_vowels = 0
    for letter in line:
        if letter in "aeyuio":
            num_vowels += 1
    return num_vowels
