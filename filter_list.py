# I can't to remove element in list and go on.
# But if i'll do copy of list for iteration, i can to remove elements
# of original list;

def filter_list(l):
    cnt = 0
    for x, item in enumerate(l[:]):
        
        if type(item) == type("string"):
        
            l.remove(item)
    return l
