numbers = input().split("; ")
num = int(input())
dict_reminders = {}
for numb in numbers:
    remind = int(numb) % num
    dict_reminders[remind] = dict_reminders.get(remind, 0) + int(numb)
print(dict_reminders)
