num_birds = int(input())
tuple_counter = []
for i in range(num_birds):
    bird = input()
    if bird not in tuple_counter:
        tuple_counter += [bird]
        tuple_counter += [1]
    else:
        tuple_counter[tuple_counter.index(bird) + 1] += 1
i = 0
while i < len(tuple_counter):
    print((tuple_counter[i], tuple_counter[i + 1]))
    i += 2
