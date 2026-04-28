num = int(input())
dict_owner = {}
for i in range(num):
    cat_name, owner, toy_name = input().split()
    dict_owner[owner] = dict_owner.get(owner, []) + [{"cat": cat_name, "toy": toy_name}]
print(dict_owner)
