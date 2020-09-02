# Starting in the top left corner of a 2×2 grid,
# and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.


# How many such routes are there through a 20×20 grid?

#----------------------------------------------
dictionary = {}


def routes(a, b):
    """returns number of routes in a*b grid"""
    if (a,b) in dictionary.keys():
        return dictionary[(a,b)]
    else:
        if a == b == 1:
            dictionary[(a,b)] = 2
            return 2
        elif a == 1:
            dictionary[(a,b)] = 1 + routes(a, b - 1) 
            return 1 + routes(a, b - 1) 
        elif b == 1:
            dictionary[(a,b)] = 1 + routes(a - 1, b) 
            return 1 + routes(a - 1, b)
        else:
            dictionary[(a,b)] = routes(a - 1, b) + routes(a, b - 1)
            return routes(a - 1, b) + routes(a, b - 1)
 
print(routes(20,20))