def find_outlier(integers):
    odd = 0
    even = 0
    for i in integers:
        if i % 2 == 0:
            even += 1
        elif i % 2:
            odd += 1
    if odd > even:
        for i in integers:
            if i % 2 == 0:
                return i
    elif even > odd:
        for i in integers:
            if i % 2:
                return i
