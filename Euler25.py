'''
    Gets the fibonacci number at 'index'
    Assumes 0th term is 0, 1st is 1, 2nd is 1, etc...
'''
def get_fib(index):

    # used to traverse fibonacci sequence
    a = 0
    b = 1

    # a becomes b, b becomes sum of a and b
    for i in range(index):
        a, b = b, a + b

    return a

'''
    Gets length of digits making up number
    get_len(89) is 2
'''
def get_len(number):

    # easier than dividing by 10 until 0
    return len(str(number))

'''
    Finds the first fibonacci number with over 1000 digits
'''
def find_num():
    for i in range(10000):

        # if length of the number is over 1000
        if get_len(get_fib(i)) >= 1000:
            return i