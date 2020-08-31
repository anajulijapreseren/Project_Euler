def square_of_the_sum(N):
    return ((N * (N + 1)) / 2) ** 2

def sum_of_the_squares(N):
    return (N * (N + 1) * (2 * N + 1)) / 6    

def difference(N):
    diff = square_of_the_sum(N) - sum_of_the_squares(N)
    print("diff is: ",diff)
    return diff

difference(100)