'''
at first we are creating variable which will keep current value
if current value and next value the same - continue. Else adding 
this element to list
'''

def unique_in_order(iterable):
    res = list()
    sym = None
    for item in iterable:
        if sym != item:
            res.append(item)
            sym = item
    return res
    
print(unique_in_order('AAAABBBCCDAABBB'))
