# Given natural number N, calculate the sum of all multiples of 3 and 5 below N

# sum takes one argument, natural number N and returns sum of all multiples of 3 and 5 below N
# method runs over all i from 1 to N
# for each i we determine if it is multiple of 3 or 5
# it it is, we add it to sum
# finaly we return the sum

def sum(N):
    sum = 0
    for i in range(1,N ):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i    
    print("Sum is: ", sum)
    return sum

sum(1000)