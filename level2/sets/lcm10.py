import math

line = input()
set_let = set(line)
unic_let = len(set_let)
numbers = []
num_bits = math.ceil(math.log2(unic_let))
print(num_bits * len(line))
