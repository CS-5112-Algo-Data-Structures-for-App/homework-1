'''
Problem 4b

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n).
'''
def most_frequent_difference_b(values: list, d_mode: int) -> int:
    '''
    given a list of integers and a delta mode, find the number of pairs in values that have a difference of delta mode
    in O(n) time and O(n) space
    :param values: list of integers
    :param d_mode: interger
    :return: number of valid pairs
    '''

    values_dict = {}
    res = 0

    # setup a dictionary to keep track of the number of times a value appears in the list
    for value in values:
        if value not in values_dict:
            values_dict[value] = 0
        values_dict[value] += 1

    for value in values:
        # if the value + d_mode is in the dictionary, we have a pair
        if value + d_mode in values_dict:
            # if d_mode is not 0, we can just add the number of times the value + d_mode appears in the list to the res
            # since we can form that many pairs
            if d_mode != 0:
                res += values_dict[value + d_mode]
            # if d_mode is 0, we need to subtract 1 from the number of times the value + d_mode appears in the list
            # since we cannot form a pair with the same number but with all other duplicates
            else:
                res += values_dict[value + d_mode] - 1

    return res

# should be 4
# delta_freq = most_frequent_difference_b([2,2,4,4], 2)
