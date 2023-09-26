'''
Problem 4a

input: 
    values -- list of integers. 
    d_mode -- most frequent delta.
output: integer containing the frequency of d_mode.

TODO: implement your solution in Θ(n log n).
'''
def most_frequent_difference_a(values: list, d_mode: int) -> int:
    '''
    given a list of integers and a delta mode, find the number of pairs in values that have a difference of delta mode
    in O(nlogn) time and O(1) space
    :param values: list of integers
    :param d_mode: interger
    :return: number of valid pairs
    '''
    # sort the list
    values.sort()
    res = 0

    new_list = []
    # make a list where all duplicates of a number is represented as (number, number of duplicates) in O(n) time
    # ie. [1,1,1,2,2,3] -> [(1,3), (2,2), (3,1)]
    i = 0
    while i < len(values):
        j = i + 1
        # find duplicates
        while j < len(values) and values[j] == values[i]:
            j += 1
        no_of_copies = j - i
        new_list.append((values[i], no_of_copies))
        i = j


    for i in range(len(values)):
        # binary search on our special deduped list for the value that is d_mode away from values[i]
        target = values[i] + d_mode
        idx = binary_search(new_list, target)
        if idx != -1:
            if d_mode != 0:
                res += new_list[idx][1]
            else:
                res += new_list[idx][1] - 1

    return res


def binary_search(values: list[tuple[int, int]], target: int) -> int:
    '''
    given a sorted list of list with 2 integers and a target, return the index of the target in the list based off the 1st integer
    :param values: list of integers
    :param target: integer
    :return: index of target in values
    '''
    left = 0
    right = len(values) - 1

    while left <= right:
        mid = (left + right) // 2
        if values[mid][0] == target:
            return mid
        elif values[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# should be 4
delta_freq = most_frequent_difference_a([2,2,4,4], 2)
