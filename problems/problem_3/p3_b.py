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
        if len(lst) == 1:
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
        ranks = list(range(n))
        reorder_ranks = sorted(ranks, key=lambda x: lst[x])

        _, inversions = helper(reorder_ranks, delta)
    return inversions

def number_of_large_inversions_3c(file, delta) -> int:
    ordering = []
    with open(file, "r") as f:
        n = int(f.readline())
        ranks = f.readline().split()
        for x in ranks:
            ordering.append(int(x))

    ranks = list(range(n))
    reorder_ranks = sorted(ranks, key=lambda x: ordering[x])

    _, inversions = divide_and_conquer(reorder_ranks, delta)
    return inversions

# Θ(n log n) implementation, divide and conquer
def divide_and_conquer(sub_ranks, delta) -> (list, int):
    if len(sub_ranks) <= 1:
        return sub_ranks, 0

    mid = len(sub_ranks) // 2
    left_ranks = sub_ranks[:mid]
    right_ranks = sub_ranks[mid:]

    left_sort, left_inv = divide_and_conquer(left_ranks, delta)
    right_sort, right_inv = divide_and_conquer(right_ranks, delta)

    i = j = inv = 0
    while i < len(left_sort) and j < len(right_sort):
        if left_sort[i] <= right_sort[j] + delta:
            i += 1
        else:
            inv += len(left_sort) - i
            j += 1

    sorted_ordering = []
    i = j = 0
    while i < len(left_sort) and j < len(right_sort):
        if left_sort[i] < right_sort[j]:
            sorted_ordering.append(left_sort[i])
            i += 1
        else:
            sorted_ordering.append(right_sort[j])
            j += 1

    while i < len(left_sort):
        sorted_ordering.append(left_sort[i])
        i += 1

    while j < len(right_sort):
        sorted_ordering.append(right_sort[j])
        j += 1

    return sorted_ordering, left_inv + right_inv + inv

def number_of_large_inversions_3a(lst, delta) -> int:
    n = len(lst)
        
    inversions = 0
        
    lst_sorted = sorted(lst)
    # q: explain what is happening here
    # a: for each element in the sorted list, find the index of that element in the original list.
    #    compare that index to the index of every element in the sorted list that comes after it.
    #    if the index of the element in the sorted list is greater than the index of the element in the original list,
    #    then we have an inversion.
    for x_val in lst_sorted:
        x_idx = lst_sorted.index(x_val)
        for y_val in lst_sorted[x_idx+1:]:
            x_j = lst.index(x_val)
            y_j = lst.index(y_val)
            if x_j > y_j + delta:
                inversions += 1
                
    return inversions

import os

print(number_of_large_inversions_3b(os.path.dirname(os.getcwd()) +  r'/tests/input/test_p3_public_n4_2.txt',1))

# ans 2