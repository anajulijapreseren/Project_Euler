# Starting with the number 1 and moving to the right in a clockwise direction
#  a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

#----------------------------------------------------
#we look at numbers on diagonals and notice following rule, that is used in formula:
diagonal_sum = 1
minus = 2
for i in range(3, 1002, 2):
    square = i **2
    diagonal_sum += square #upper right diagonal has squares of odd numbers
    diagonal_sum += square - minus
    diagonal_sum += square - 2 * minus
    diagonal_sum += square - 3 * minus
    minus += 2
print(diagonal_sum)
    
