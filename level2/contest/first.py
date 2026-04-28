hights = {}
line = input()
while line:
    line_list = line.split()
    first = int(line_list[0]) // 100 * 100
    hights[first] = hights.get(first, set())
    for i in range(1, len(line_list)):
        hights[first].add(int(line_list[i]))
    line = input()
num = int(input())
for _ in range(num):
    request = int(input())
    if request in hights:
        id_req = list(hights[request])
        req = sorted(id_req)
        print(*req, sep=", ")
    else:
        print("No info")
