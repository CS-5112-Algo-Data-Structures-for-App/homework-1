'''
Problem 3b

input: 
    file -- contains 2 lines. The first one has an integer n.
    The second one has an ordering of the integers from 1 to n (see README). 
    delta -- bound for ranking significance.
output: Number of large inversions. 

TODO: implement a Θ(n log n) as described in the homework.
'''
def number_of_large_inversions_3b(file, delta) -> int:
    def helper(lst, delta):
        if len(lst) <= 1:
            return lst, 0
        else:
            a_lst = lst[:len(lst)//2]
            b_lst = lst[len(lst)//2:]

            # Sort and count
            a_lst, inv_left = helper(a_lst, delta)
            b_lst, inv_right = helper(b_lst, delta)

            inv = inv_left + inv_right
            # merge and count
            i = 0
            j = 0
            while i < len(a_lst) and j < len(b_lst):
                if a_lst[i] > b_lst[j] + delta:
                    inv += len(a_lst) - i
                    j += 1
                else:
                    i += 1

            merge_lst = a_lst + b_lst
            merge_lst.sort()

            return merge_lst, inv

    n = 0
    with open(file, "r") as f:
        n = int(f.readline())
        lst = [int(element) for element in list(f.readline().split())]
        sorted_ranks = sorted(list(range(n)), key=lambda x: lst[x])

        _, inversions = helper(sorted_ranks, delta)
    return inversions