children = set(input().split())
ch_cars = set(input().split())
ch_balls = set(input().split())
union_set = ch_balls | ch_cars
diff_set = children - union_set
print(*list(diff_set))
