'''
Problem 2

input: Integer M and a list of intervals [a, b].
output: List of list of integers composing the covering.

TODO: implement a correct greedy algorithm from the homework.
'''
def interval_covering(M: int, intervals: list) -> list:
#     J_lst = []
#     c = 0

#     intervals.sort()

#     while M > c:

#         intervals_w_c_lst = []
#         for interval in intervals:
#             if interval[0] > c:
#                 break
#             else:
#                 intervals_w_c_lst.append(interval)
# #         O(x) -> x is the num of intervals in intervals_w_c_lst
#         J_lst.append(max(intervals_w_c_lst))

#         c = max(J_lst)[1]

#         for interval_c in intervals_w_c_lst:
#             intervals.remove(interval_c)
    
#     return J_lst
    
    return_list = []
    intervals.sort()