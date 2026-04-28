genom = input()
dict_par = {}
for i in range(len(genom) - 1):
    dict_par[genom[i]] = dict_par.get(genom[i], dict())
    dict_par[genom[i]][genom[i + 1]] = dict_par[genom[i]].get(genom[i + 1], 0) + 1
result_dict = {}
for nucl in dict_par:
    max_num = max(dict_par[nucl].values())
    line_nuc = ""
    for k, n in dict_par[nucl].items():
        if n == max_num:
            line_nuc += k
    result_dict[nucl] = result_dict.get(nucl, "".join(sorted(line_nuc)))
print(result_dict)
