text = input()
hop = int(input())
way = ""
for i in range(0, len(text), hop):
    way += text[i]
print(way)
