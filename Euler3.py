'''
    Use sieve of Eratosthenes to fill 'prime_set' with prime ints
'''
def populate(prime_set, upper):

    # delet all contents of the prime set
    prime_set.clear

    # contains set of all composite numbers less than 'upper'
    comp_set = set()

    # manually add 0 and 1
    comp_set.add(0)
    comp_set.add(1)

    # Only square root of 'upper' need to be checked (not sure why)
    for i in range(2, (int)(upper ** .5) + 1):

        # if 'i' has not already been proven to be composite
        if i not in comp_set:

            # add every multiple of 'i' that goes into 'upper' to composite set
            for j in range(i, (upper - 1) / i + 1):
                comp_set.add(i * j)

    # add every number not proven to be composite to prime set
    for i in range(upper):
        if i not in comp_set:
            prime_set.add(i)

'''
    Determines largest factor of 'number' contained in 'prime_set'
'''
def find_biggest_factor(prime_set, number):

    # keeps track of largest factor found
    current_largest = 0

    # traverse primes
    for i in range(len(prime_set)):
        if i in prime_set:

            # replace 'current_largest' if 'i' is bigger and still goes into 'number'
            if i > current_largest and number % i == 0:
                current_largest = i

    return current_largest

def main():
    my_set = set()

    populate(my_set, 100000)

    print find_biggest_factor(my_set, 600851475143)
    
main()
    




