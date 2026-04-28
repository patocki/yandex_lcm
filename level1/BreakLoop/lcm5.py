num = int(input())
while num > 0:
    line = str(num)
    if len(line) != 1:
        sum = 0
        for i in range(len(line)):
            sum += int(line[i])
        print(sum)
        num = int(input())
    else:
        num = int(input())
        continue
