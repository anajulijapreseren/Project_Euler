#There are exactly ten ways of selecting three from five, 12345:
#
#123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
#In combinatorics, we use the notation, (53)=10.
#
#In general, (nr)=n!/r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.
#
#It is not until n=23, that a value exceeds one-million: (2310)=1144066.
#
#How many, not necessarily distinct, values of (nr) for 1≤n≤100, are greater than one-million?

#------------------------------------------------------------------
def factorial(n): 
    if n < 0: 
        return 0
    elif n == 0 or n == 1: 
        return 1
    else: 
        fact = 1
        while(n > 1): 
            fact *= n 
            n -= 1
        return fact 

#ugotovimo, od katerih stevil dalje se nam splaca gledat:
#i = 1
#while factorial(i) < 1000001:
#    i += 1
#print(i)

#prvih 9 števil torej ne gledamo

a = 0
for n in range(9, 101):
    for r in range(1, n + 1):
        if factorial(n) / (factorial(r) * factorial (n - r)) > 1000000:
            a += 1
print(a)
