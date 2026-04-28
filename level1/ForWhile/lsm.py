line = input()
trueline = line
leng = len(line)
maxline = line
while True:
    if leng <= len(line):
        leng = len(line)
        trueline = line
    line = input()
    if line == "":
        break
print(f"{trueline}, {leng}")
