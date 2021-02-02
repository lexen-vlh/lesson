def up(a):
    return a.title()

print(up("abcde"))

def mup(a):
    l = a.split(' ')
    r = ""
    for i in l:
        r += up(i) + ' '
    return r

print(mup('abcde fghij klmno'))
