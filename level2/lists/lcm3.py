num_words = int(input())
words = []
res = []
for i in range(num_words):
    words.append(input())
num_indx = int(input())
for i in range(num_indx):
    res.append(words[int(input())])
print(*res)
