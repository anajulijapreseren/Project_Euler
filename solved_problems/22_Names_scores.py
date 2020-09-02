# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over
# five-thousand first names, begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, 
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

with open ('22_names.txt') as dat:
    names = dat.read().split(',')

names.sort()


dictionary = {chr(i+64):i for i in range(1,27)}

def value_of_name(name):
    value = 0
    name = name[1:-1]
    for i in range(0, len(name)):
        letter = str(name)[i]
        value += dictionary[letter]
    return value

name_scores = 0
i = 1
while i <= len(names):
    name_scores += value_of_name(names[i - 1]) * i
    i += 1
print(name_scores)

