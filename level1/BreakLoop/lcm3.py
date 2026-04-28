num = int(input())
result = 0
fish = "карас"
fish2 = "лещ"
fish3 = "окун"
for i in range(num):
    line = input()
    if "барракуда" in line:
        result = "Спасайся!"
        break
    if fish in line or fish2 in line or fish3 in line:
        result += 1
print(result)
