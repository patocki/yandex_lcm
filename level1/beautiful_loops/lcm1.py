num_stars = int(input())
spaces = 2
print("--" + "*" * num_stars + "--")
while True:
    if num_stars <= 0:
        break
    num_stars -= 2
    spaces += 1
    linestars = " " * spaces + "*" * num_stars + " " * spaces
    print(linestars)
