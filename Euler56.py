# Sums the digits in n
def get_dig_sum(n):
    the_sum = 0

    # string conversion to isolate each digit
    for dig in str(n):
        the_sum += int(dig)

    return the_sum


# Returns the maximum digit sum in 1 to 100
def find_max():
    current_max = 0

    # for every a and b combo from 1 to 100 (exclusive)
    for a in range(1, 100):
        for b in range(1, 100):

            # save dig sum of a^b
            candidate = get_dig_sum(a ** b)

            # replace current_max if applicable
            if candidate > current_max:
                current_max = candidate

    return current_max
