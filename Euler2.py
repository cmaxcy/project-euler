'''
    Iteratively gets fibonacci number at 'index'
'''
def get_fib(index):

    # first and second fibonacci terms given
    a = 0
    b = 1

    # a = b, b = a + b
    for i in range(index):
        a, b = b, a + b

    return b

'''
    Sums up numbers in a list
'''
def get_sum(list):

    # begin sum at 0
    sum = 0

    # traverse list and add contents to sum
    for i in list:
        sum += i

    return sum

'''
    Uses get_fib() to generate a list of all fib numbrs less than 4 * 10^6
'''
def get_evens():

    # used to store fibonacci numbers
    fib_list = []

    # used to enter numbers
    index = 0
    
    while (get_fib(index) < 4000000):

        # if fibonacci numbers is even add it to list
        if get_fib(index) % 2 == 0:
            fib_list.append(get_fib(index))

        # increment index regardless
        index += 1

    return get_sum(fib_list)

def main():
    print get_evens()