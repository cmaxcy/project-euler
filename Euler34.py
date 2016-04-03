# Returns the factorial of n using recursion, negatives returned as 1
def get_fact(n):
    if n < 1:
        return 1

    return get_fact(n - 1) * n


# Determines whether or not the number n is the same as the sum of the factorial of its digits
def is_fact_sum(n):

    current_sum = 0

    # convert n to string, analyze each char(digit)
    for dig in str(n):

        # add the factorial of the digit to the sum
        current_sum += get_fact(int(dig))

    return current_sum == n


# Sums all n < limit who pass is_fact_sum(n)
def get_total(limit):

    total_sum = 0

    for i in range(limit):

        # if number qualifies, add it to total_sum
        if is_fact_sum(i):
            total_sum += i

    return total_sum

print(get_total(100000))
