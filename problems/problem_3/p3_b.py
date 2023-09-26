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
    n = 0
    
    with open(file, "r") as f:
        n = int(f.readline())
        lst = [int(element) for element in list(f.readline().split())]
    
    if len(lst) == 1:
        return 0
    else:
        inversions = 0
        
    # inversions = number_of_large_inversions_3a(lst,delta)
        a_lst = lst[:len(lst)//2]
        b_lst = lst[len(lst)//2:]
        
        # Sort and count
        inversions = inversions + number_of_large_inversions_3a(a_lst,delta)
#         # print(a_lst)
        # print('a inv: ' + str(inversions))
        inversions = inversions + number_of_large_inversions_3a(b_lst,delta)
#         # print(b_lst)
        # print('b inv: ' + str(inversions))
        a_lst.sort()
        b_lst.sort()
        
        
        # merge and count
        i = 0
        j = 0
        while i < len(a_lst) and j < len(b_lst):
            
            
            if a_lst[i] > b_lst[j] + delta:
                inversions += 1
                j += 1
            else:
                i += 1
        
        # while j < len(b_lst):
        #     if i > len(a_lst):
        #         inversions += (len(b_lst)-j)
        #         break
            
    return inversions   

def number_of_large_inversions_3a(lst, delta) -> int:
    n = len(lst)
        
    inversions = 0
        
    lst_sorted = sorted(lst)
    
    for x_val in lst_sorted:
        x_idx = lst_sorted.index(x_val)
        for y_val in lst_sorted[x_idx+1:]:
            x_j = lst.index(x_val)
            y_j = lst.index(y_val)
            if x_j > y_j + delta:
                inversions += 1
                
    return inversions

import os

print(number_of_large_inversions_3b(os.path.dirname(os.getcwd()) +  r'/tests/input/test_p3_public_n4_1.txt',1))

# ans 2