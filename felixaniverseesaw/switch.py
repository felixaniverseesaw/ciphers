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
        'v':'v'
    }

    def switch(x):
        if "qwertyuiopasdfghjklzxcvbnm".find(x) == -1:
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
