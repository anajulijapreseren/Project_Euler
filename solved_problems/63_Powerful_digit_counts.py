# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number,
#  134217728=89, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

#---------------------------------------------
#one digit number:
#9**1 = 9
#9**2= 81
#9**3= 729
#ok, length is the same as power

#two digit number:
#10**1 = 10
#10**2 = 100
#not ok, same for 3, 4...digit numbers

#so we have to look at one digit numbers

number_of_possibilities = 0

for i in range(1, 10):
    power = 1
    while True:
        if power == len(str(i ** power)):
            number_of_possibilities += 1
        else:
            break
        power += 1

print(number_of_possibilities)
