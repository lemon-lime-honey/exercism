from secrets import randbelow

def private_key(p):
    a = 0
    while a in (0, 1):
        a = randbelow(p)
    return a

def public_key(p, g, private):
    return ((g ** private) % p)

def secret(p, public, private):
    return ((public ** private) % p)
