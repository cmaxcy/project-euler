'''
    Iteratively calculates factorial of 'n'
'''
def get_fact(n):
    
    out = 1

    # every number <= 'n' is multiplied together
    for i in range(1, n + 1):
        out *= i

    return out 

'''
    Calculates the number of ways of selecting 'r' from 'n'
    Example: get_comb(5, 3) == 10
'''
def get_comb(n, r):
    return get_fact(n) / (get_fact(r) * get_fact(n - r))

'''
    Calculate how many combinatoric values are greater than one million for 1 <= n <= 100
'''
def get_count():

    # used to store how many combinations have exceeded one million
    count = 0

    # For every number <= 100, cycle through each positive number less than it
    for a in range(1, 101):
        for b in range(a, 0, -1):

            # if the combination is greater than one million
            if get_comb(a, b) > 1000000:

                # increment count
                count += 1

    return count