hours = int(input())
min = int(input())
hut = int(input())
sum_minutes = min + hut
while hut != 0:
    hut = int(input())
    sum_minutes += hut
    if sum_minutes >= 60:
        hours += sum_minutes // 60
        sum_minutes = sum_minutes % 60
    if hours >= 24:
        print("Новый день!")
        break
else:
    print(f"{hours}:{sum_minutes:02d}")
