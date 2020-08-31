import math

def smallest_multiple(n):
    for i in range (n, math.factorial(n) + 1):
        vsota = sum((i % x) for x in range (1, n + 1))
        if vsota == 0:
            return i

def rok(n):
    for i in range (n, math.factorial(n) + 1):
        modelOdleti = False;
        for x in range (1,n+1):
            if (i % x != 0):
                    modelOdleti = True;
                    break;
        if (not modelOdleti):
             return i            


# smallest_multiple(5)
rok(20)