start = int(input())
end = int(input())
sum = 0
for j in range(start, end + 1):
    for i in range(2, int(j**0.5) + 1):
        if j % i == 0:
            sum += i
            if j // i != i:
                sum += j // i
    print(sum)
    sum = 0
