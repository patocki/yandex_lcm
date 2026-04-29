def quarters(coord: list) -> dict[str:list]:
    res = {}
    for x, y in coord:
        if x == 0 and y == 0:
            res["X-axis"] = res.get("X-axis", [])
            res["X-axis"].append((x, y))
            res["Y-axis"] = res.get("Y-axis", [])
            res["Y-axis"].append((x, y))
        else:
            if x > 0 and y > 0:
                key = "I"
            elif x < 0 and y < 0:
                key = "III"
            elif x < 0 and y > 0:
                key = "II"
            elif x > 0 and y < 0:
                key = "IV"
            elif y == 0:
                key = "X-axis"
            elif x == 0:
                key = "Y-axis"
            res[key] = res.get(key, [])
            res[key].append((x, y))
    return res


# points = [(0, 0), (-3, -2.1), (3, 0)]
# print(quarters(points))
