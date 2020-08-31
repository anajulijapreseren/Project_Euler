#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

#-------------------------------------------------------------------------------

#števil , velikih 10000 ali več zaradi dolžine ni smiselno gledati

sez = []
for i in range(1, 10000):
    a = str(i)
    n = 1
    while len(a) < 9:
        n += 1
        a += str(n * i)
    if len(a) == 9:
        stevilo = 0
        for cifra in range(1, 10):
            if str(cifra) in a:
                stevilo += 1
        if stevilo == 9:
            sez.append(int(a))
print(max(sez))
