start = int(input())
end = int(input())
stap = int(input())
for i in range(start, end, stap):
    print(i, end=" ")
for i in range(end, start - 1, -(stap + 1)):
    print(i, end=" ")
