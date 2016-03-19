'''
    Fills set with all combinations of 'a' ^ 'b'
'''
def fill_set(list):

    # every combination of two variables 2 to 100
    for a in range(2, 101):
        for b in range(2, 101):

            # add to set
            list.add(a**b)

def get_count():

    # will be used to hold combinations
    combinations = set()

    fill_set(combinations)
    return len(combinations)