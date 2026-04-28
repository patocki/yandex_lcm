num = int(input())
statistic = []
for i in range(num):
    line = input()
    stat_line = {
        "index": i,
        "number": len(line.split()),
        "average": int(
            sum([len(word) for word in line.split()]) / len(line.split()) * 100
        ),
        "syllable": len(
            [letter for letter in "".join(line.split()).lower() if letter in "aeyuio"]
        ),
        "largest": max(line.split()),
    }
    statistic += [stat_line]
print(statistic)
