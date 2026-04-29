def parabola(a, b, c, *args):
    res_coord = []
    for arg in args:
        x, y = arg
        if a > 0:
            if y > a * x**2 + b * x + c:
                res_coord.append(arg)
        else:
            if y < a * x**2 + b * x + c:
                res_coord.append(arg)
    return res_coord


# points = [(0, 0), (1.2, 3), (-1, -2)]
# print(parabola(1, -2, -3, *points))
