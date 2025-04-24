import time

with open('Pan_Tadeusz_frag.txt', 'r', encoding='utf-8') as f:
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

    while lewa <= prawa:
        res[lewa] = var[i]
        res[prawa] = var[i+1]
        i += 2
        lewa += 1
        prawa -=1

    if lewa == prawa:
        res[lewa] = var[i]
    return ''.join(res)


start = time.time()
print(decode_trans(code_trans(tekst)))
stop = time.time()
comp_time = stop - start
# print(f'time: {comp_time}')
