# By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
# the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
#  a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18.
#  It is not possible to try every route to solve this problem, as there are 299 altogether!
#  If you could check one trillion (1012) routes every second 
# it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

#-------------------------------------------------------------------------------

with open('numbers_in_triangle.txt') as dat:
    number = dat.read()

#splitting the number into a list
#we get a list, which elements are lines
number = number.strip().split('\n')

#we get list of lists
for i in range(1,len(number)):
	number[i] = number[i].strip().split(' ')
	number[i] = [int(x) for x in number[i]]
#we have to change first number from string to list(otherwise length doesn't work properly)
number[0] = [int(number[0])]


answer = 0
while answer == 0:
    #new line to replace last two
    new_line = []

    #number of lines
    last_length = len(number)
    if last_length == 1:
        answer = number[0]

    else:
        #last line
        last_line = number[last_length - 1]

        #second to last line
        stl_line = number[last_length - 2]
        stl_length = len(stl_line)

        for i in range(0, stl_length):
            new_element = max(int(last_line[i]), int(last_line[i + 1])) + int(stl_line[i])
            new_line.append(new_element)
        number.remove(last_line)
        number.remove(stl_line)
        number.append(new_line)
print(answer)