'''
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.
'''

def alphabet_position(text):
    string_list = list(text)
    res = []
    for i in string_list:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'): 
            res.append(ord(i) - 64)
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            res.append(ord(i) - 96)
    res = list(map(str, res))
    return (' '.join((res)))
    
print(alphabet_position("The narwhal bacons at midnight."))
