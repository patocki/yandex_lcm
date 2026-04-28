k = float(input())
b = float(input())
num = int(input())
pozition_y = 0
pozition_x = 0
i = 0
while True:
    if i == num:
        break
    axis = input()
    offset = float(input())
    if axis == "x":
        pozition_x += offset
    else:
        pozition_y += offset
    if pozition_y > (pozition_x * k + b):
        print("Up")
        break
    i += 1
    print(f"({pozition_x};{pozition_y})")
