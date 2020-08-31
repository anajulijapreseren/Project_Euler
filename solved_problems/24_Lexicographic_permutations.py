#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

#-------------------------------------------------------------------------------------------
#imamo deset števil, za vsako cifro je torej 9! permutacij
#9! = 362880

#1000000 // 362880 = 2, torej lahko izpustimo števila, ki se začnejo z 0 ali 1
#sedaj namesto 1000000 števila iščemo št na mestu 1000000 - 2*362880 = 274240, ki se začne z 2

#permutacije števil 0, 1, 3, 4, 5, 6, 7, 8, 9
# A Python program to print all  
# permutations using library function 
from itertools import permutations 
  
# Get all permutations of [0, 1, 3, 4, 5, 6, 7, 8, 9] 
perm = permutations([0, 1, 3, 4, 5, 6, 7, 8, 9]) 
  
# Print the obtained permutations
sez = [] 
for i in list(perm): 
    sez.append(i)
print(sez[274239])#damo eno st manj ker zacnemo pri 0