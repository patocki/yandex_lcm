num_mount = int(input())
zero_count = 0
min_arr = 0
result = ""
current_mountain = int(input())
mininaml_mount = current_mountain
while zero_count != num_mount:

    if current_mountain < 0:
        result = "Ущелье!"
        break
    current_mountain = int(input())
    if current_mountain == 0:
        zero_count += 1
        continue
    if current_mountain <= mininaml_mount:
        mininaml_mount = current_mountain
        result = f"Наименьшая высота {mininaml_mount} в(о) {zero_count + 1}-м массиве."

print(result)
