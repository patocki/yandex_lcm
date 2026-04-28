travel_map = {}

while True:
    line = input().split(": ")
    if len(line) < 2:  # Если меньше 2 элементов - выходим
        break
    travel_map[line[0]] = travel_map.get(line[0], []) + [line[1]]

print(travel_map)
