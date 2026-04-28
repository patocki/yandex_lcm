date_cvet = {}
while True:
    line = input()
    if not line:
        break
    date, place = line.split("\t")
    date_cvet[place] = date_cvet.get(place, set())
    date_cvet[place].add(date)

place = input()
if place in date_cvet:
    for date in date_cvet[place]:
        print(date)
else:
    print("No data")
