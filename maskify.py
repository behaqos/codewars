def maskify(cc):
    length = len(cc) - 4
    res_list = list(cc)
    if length > 4:
        for i in range(0, (len(cc) - 4)):
            res_list[i] = '#'
        return(''.join(res_list))
    elif length <= 4:
        return (cc)
