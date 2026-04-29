beg, *line, end = input().split()
beg_l = beg.lower()
end_l = end.lower()
res = []
for word in line:
    word = word.lower()
    if end_l > word > beg_l:
        res.append(word)
print(*res)
