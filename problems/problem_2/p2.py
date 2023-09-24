'''
Problem 2

input: Integer M and a list of intervals [a, b].
output: List of list of integers composing the covering.

TODO: implement a correct greedy algorithm from the homework.
'''
def interval_covering(M: int, intervals: list) -> list:
    c = max(intervals)[1]
    J_lst = []

    while len(intervals)>0:
        
        for interval in intervals:
            if max(interval) < c:
                pass
            else:
                intervals.remove(interval)

        if len(intervals) > 0:
            latest_finish_lst = max(intervals)
            J_lst.append(latest_finish_lst)
            intervals.remove(latest_finish_lst)

            c = latest_finish_lst[0]
            
            
    return J_lst