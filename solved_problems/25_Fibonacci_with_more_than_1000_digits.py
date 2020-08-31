import math

def index(N):
    f1 = 1
    f2 = 1 
    fn = f1 + f2
    i = 3
    while math.log10(fn) < N-1: 
        i += 1
        f1 = f2
        f2 = fn
        fn = f1 + f2
    print("Index is: ", i)
    return i

index(1000)