import time

with open('Pan_Tadeusz.txt', 'r', encoding='utf-8') as f:
    tekst = f.read()


def code_trans(var):
    lewa = ''
    prawa = ''
    for i, znak in enumerate(tekst):
        if i % 2 == 0:
            prawa += znak
        else:
            lewa = znak + lewa
        res = prawa + lewa
    return res


def decode_trans(var):
    mid = (len(var) + 1) // 2
    prawa = var[:mid]
    lewa_rev = var[mid:]
    lewa = lewa_rev[::-1]

    res = ''
    for i in range(len(var)):
        if i % 2 == 0:
            res += prawa[i // 2]
        else:
            res += lewa[i // 2]

    return res


start = time.time()
print((decode_trans(code_trans(tekst))))
stop = time.time()
comp_time = stop - start
#print(f'time: {comp_time}')
