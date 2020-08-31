def is_prime(n):
    sez = []
    for i in range(1, int(n + 1)):
        if n % i == 0:
            sez += [i]
    return len(sez) == 2

slovar = {1:2}#slovar oblike n:n-to prastevilo
def next_prime(n):
    """poisce naslednje prastevilo za prastevilo n"""
    if not is_prime(n):
        print('n ni prastevilo')
    while not is_prime(n+1):
        n += 1
    return n + 1


def prastevilo(x):
    """vrne x-to prastevilo"""
    if x in slovar.keys():
        return slovar[x]
    else:
        max_indeks = max(slovar.keys())
        max_prastevilo = slovar[max_indeks]
        slovar[int(max_indeks + 1)] = next_prime(max_prastevilo)
        return prastevilo(x) 


#postopoma vstavljamo vecja stevila in polnimo slovar, da pridemo do 10001
