num = int(input())
texts = []
for i in range(num):
    line = input()
    texts.append(line.split())
maximum_list = None
max_l = texts[0]
for j in range(num - 1):
    if len(texts[j + 1]) >= len(max_l):
        max_l = texts[j + 1]
print(" ".join(max_l).title())
