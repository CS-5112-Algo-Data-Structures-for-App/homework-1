'''
Problem 2

input: Integer M and a list of intervals [a, b].
output: List of list of integers composing the covering.

TODO: implement a correct greedy algorithm from the homework.
'''
def interval_covering(M: int, intervals: list) -> list:
    intervals.sort()
    J = []
    c = 0
    max_val = intervals[0]
    i = 0
    while i in range(len(intervals)):
        if c >= intervals[i][0]:
            if intervals[i][1] > max_val[1]:
                max_val = intervals[i]
            i += 1
        else:
            J.append(max_val)
            c = max_val[1]
    if max_val not in J:
        J.append(max_val)
    return J
