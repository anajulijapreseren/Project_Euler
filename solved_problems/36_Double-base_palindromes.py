#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

#(Please note that the palindromic number, in either base, may not include leading zeros.)

#-------------------------------------------------------------------------------------------

def palindrom(niz):
    return niz == niz[::-1]

sez_10_palindromov = []
for i in range(1,1000000):
    if palindrom(str(i)):
        sez_10_palindromov.append(i)
#print(sez_10_palindromov)

#izražanje binarnih števil:
#>>> bin(173)
#'0b10101101'

#print(bin(173)[2:])

sez_2_in_10 = []
for i in sez_10_palindromov:
    binary = bin(i)[2:]
    if binary == binary[::-1]:
        sez_2_in_10.append(i)
print(sum(sez_2_in_10))