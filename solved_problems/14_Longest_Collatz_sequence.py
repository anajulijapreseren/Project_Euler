# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.
#-------------------------------------------------------------------------------------------
def len_of_colatz(a):
    mylist=[a]
    while a != 1:
        if a%2 == 0:
            a = a/2
        else:
            a = a*3 + 1
        mylist.append(a) 
    return len(mylist)

best_n = 0
maxlen = 0
for i in range(1000000, 1, -1):
    length = len_of_colatz(i)
    if length > maxlen:
        best_n = i
        maxlen = length
print(best_n)

#could use some optimisation

