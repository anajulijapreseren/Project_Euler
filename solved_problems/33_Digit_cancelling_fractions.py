# The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
# which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, 
# less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.

#--------------------------------------------
def contain_same_number(a,b):
    """tells us if two numbers between 9 and 100 have two same numbers in them"""
    list_a = [str(a)[0], str(a)[1]]
    list_b = [str(b)[0], str(b)[1]]
    for i in list_a:
        if i in list_b:
            return True
    return False

def delete_same_number(a,b):
    list_a = [str(a)[0], str(a)[1]]
    list_b = [str(b)[0], str(b)[1]]
    for i in list_a:
        if i in list_b:
            list_a.remove(i)
            list_b.remove(i)
    return int(list_a[0]) / int(list_b[0])


product = 1
for a in range(10, 100):
    for b in range(10, 100):
        if a != b and contain_same_number(a,b):
            if b % 10 != 0:
                maybe_right = delete_same_number(a, b)
                right = a / b
                if maybe_right == right and right < 1:
                    product *= right


print(product)
#[0.25, 0.2, 0.4, 0.5] = [1/4, 1/5, 2/5,1/2]
#product:0,01 --> 1/100



