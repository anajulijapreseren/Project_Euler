def sum(N):
    sum = 0
    f1 = 1
    f2 = 2 
    sum += f2
    fn = f1 + f2
    while fn < N: 
        if (fn % 2) == 0:
            sum += fn
        f1 = f2
        f2 = fn
        fn = f1 + f2     
    print("Sum is: ", sum)
    return sum

sum(4000000)