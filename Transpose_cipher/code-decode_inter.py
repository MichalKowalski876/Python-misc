import time

with open('pan_tadeusz_fragment.txt', 'r', encoding='utf-8') as f:
    tekst = f.read()


def code_trans(var):
    res = ''
    while len(var) >= 2:
        res += var[0] + var[-1]
        var = var[1:-1]
    return res + var


def decode_trans(var):
    res = [''] * len(var)
    lewa = 0
    prawa = len(var) - 1
    i = 0

    while lewa < prawa:
        res[lewa] = var[i]
        res[prawa] = var[i+1]
        i += 2
        lewa += 1
        prawa -=1

    if lewa == prawa:
        res[lewa] = var[i]
    return ''.join(res)


start_code = time.time()
code_trans(tekst)
stop_code = time.time()

szyfr = code_trans(tekst)

start_decode = time.time()
decode_trans(code_trans(tekst))
stop_decode = time.time()

print(f'Czas szyfrowania: {stop_code - start_code},   czas odszyfrowania: {stop_decode - start_decode},   suma: {stop_decode-start_code}')
