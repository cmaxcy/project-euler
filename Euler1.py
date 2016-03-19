'''
    Sums all numbers less than 'upper' that are divisible by 3 or 5
'''
def sum_numbers(upper):

    # keep track of sum
    sum = 0

    for i in range(1,upper):

        # is number cleanly divisible by 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum

print sum_numbers(1000)
