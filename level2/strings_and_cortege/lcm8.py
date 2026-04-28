num_lines = int(input())
for i in range(num_lines):
    line = input()
    if line[0].isupper():
        line = line[::-1]
        print(line.capitalize())
    else:
        line = line[: line.rfind(" ")]
        print(line.upper())
