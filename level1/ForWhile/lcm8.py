beg = int(input())
end = int(input())
st = 10
if beg - end > 0:
    st = -10
    ended = end - 10
else:
    st = 10
    ended = end + 10
for i in range(beg, ended, st):
    print(i)
