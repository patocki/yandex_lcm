dict_pgs = {}
line = input()
while line:
    name, genre, pages = line.split(" - ")
    dict_pgs[genre] = dict_pgs.get(genre, 0) + int(pages)
    line = input()
print(dict_pgs)
