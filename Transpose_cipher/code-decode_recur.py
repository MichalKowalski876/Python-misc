import time
import sys


sys.setrecursionlimit(20000)

with open('pan_tadeusz_fragment.txt', 'r', encoding='utf-8') as f:
    tekst = f.read()

def code_trans(var):
    if len(var) >= 2:
        return var[0] + var[-1] + code_trans(var[1:-1])
    else:
        return var

def decode_trans(var, lewa=0, prawa=None, i=0, res=None):
    if res is None:
        res = [''] * len(var)
        prawa = len(var) - 1
    if lewa > prawa:
        return ''.join(res)
    res[lewa] = var[i]
    i += 1

    if lewa != prawa and i < len(var):
        res[prawa] = var[i]
        i += 1
    return decode_trans(var, lewa + 1, prawa - 1, i, res)


start_code = time.time()
code_trans(tekst)
stop_code = time.time()

szyfr = code_trans(tekst)

start_decode = time.time()
decode_trans(code_trans(tekst))
stop_decode = time.time()

print(f'Czas szyfrowania: {stop_code - start_code},   czas odszyfrowania: {stop_decode - start_decode},   suma: {stop_decode-start_code}')
