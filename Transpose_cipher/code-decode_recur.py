import time
import sys


sys.setrecursionlimit(20000)

with open('Pan_Tadeusz_frag.txt', 'r', encoding='utf-8') as f:
    tekst = f.read()

def code_trans(var):
    if len(var) >= 2:
        return var[0] + var[-1] + code_trans(var[1:-1])
    else:
        return var

def decode_trans(var):
    res = [''] * len(var)
    lewa = 0
    prawa = len(var) - 1
    i = 0
    while lewa <= prawa:
        if i < len(var):
            res[lewa] = var[i]
            i += 1
        if i < len(var) and lewa != prawa:
            res[prawa] = var[i]
            i += 1

        lewa += 1
        prawa -= 1

    return ''.join(res)

print(decode_trans(code_trans(tekst)))