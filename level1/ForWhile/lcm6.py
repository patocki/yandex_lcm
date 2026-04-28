beg = int(input())
end = int(input())
for i in range(beg, end + 1):
    print("*" * i)
for i in range(end - 1, beg - 1, -1):
    print("*" * i)
