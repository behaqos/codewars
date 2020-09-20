def narcissistic( value ):
    # Code away
    res = list()
    i = 0
    cp = value
    while (value):
        res.append(int(value) % 10)
        value /= 10
        value = int(value)
        i += 1
    a = 0
    length = len(res)
    for i in res:
        a = (i ** length) + a
    if (a == cp):
        return True
    else:
        return False
        
