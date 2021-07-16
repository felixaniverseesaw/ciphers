"""
A sort-of cipher made by Joshua Soh, 2021.
"""
def sw():
    inp = input('enter string: ').lower()
    outp = ""

    switcher = {
        'q':'p',
        'w':'o',
        'e':'i',
        'r':'u',
        't':'y',
        'a':'l',
        's':'k',
        'd':'j',
        'f':'h',
        'g':'g',
        'z':'m',
        'x':'n',
        'c':'b',
        'v':'v',
        '1':'0',
        '2':'9',
        '3':'8',
        '4':'7',
        '5':'6',
        '!':')',
        '@':'(',
        '#':'*',
        '$':'&',
        '%':'^',
        '~':'`',
        '<':'>',
        ',':'.',
        ':':';',
        "'":'"',
        '/':'\\',
        '{':']',
        '}':'[',
        '|':'?'
    }

    def switch(x):
        if "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()~`:;'\".,<>?/|\\{}[]".find(x) == -1:
            return x
        else:
            try:
                xer = switcher[x]
                return switcher[x]
            except:
                for inpi, outpi in switcher.items():
                    if outpi == x:
                        return inpi

    for n in inp:
        outp += str(switch(str(n)))

    print(outp)
    
    sw()
sw()
