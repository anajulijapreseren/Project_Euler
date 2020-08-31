#The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

#Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

#------------------------------------------------------------------
z = 10405071317

a = 0
for i in range(11, 350):
    a += i**i
a = a % (10**10)


b = 0
for i in range(350, 700):
    b += i**i
b = b % (10**10)

c = 0
for i in range(700, 1000):
    c += i**i
c = c % (10**10)

print((z + a + b + c) % (10 ** 10))
