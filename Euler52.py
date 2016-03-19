'''
    Determines whether 2 lists contain the same numbers
    Only applicable for solely numerical lists
'''
def are_match(list1, list2):
    
    # if lengths are unequal, lists are unequal
    if len(list1) != len(list2):
        return False

    # if any index differs, lists are different
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    # lists must be identical
    return True

'''
    Generates and returns an array with the element indexes representing the counts of each digit
'''
def to_list(number):

    # blank list of length 10 created
    num_list = []
    for i in range(10):
        num_list.append(0)

    # indexes incremented based on digit frequency
    for char in str(number):
        num_list[int(char)] += 1

    return num_list

'''
    Determine if 'number' multiplies by itself 2, 3, 4, 5, 6 times remains a permutation
'''
def is_peru(number):

    # convert number to list with indexes representing frequency of digits
    num_list = to_list(number)

    # try numbers 2 through 6 inclusive
    for i in range(2, 7):

        # list used to check digit frequency
        num_list_compare = to_list(number * i)

        # if digit frequencies are not the same, 'number' is mot permutation
        if not are_match(num_list, num_list_compare):
            return False
    
    # number is permutation
    return True

def main():
    for i in range(1, 1000000):
        if is_peru(i):
            print i
            break