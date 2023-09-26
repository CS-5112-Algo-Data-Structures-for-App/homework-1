'''
Problem 3a

input: 
    file -- contains 2 lines. The first one has an integer n.
    The second one has an ordering of the integers from 1 to n (see README). 
    delta -- bound for ranking significance.
output: Number of large inversions. 

TODO: implement a Θ(n^2) as described in the homework.
'''
def number_of_large_inversions_3a(file, delta) -> int:
    n = 0

    with open(file, "r") as f:
        n = int(f.readline())
        lst = [int(element) for element in list(f.readline().split())]
        
    inversions = 0
    
            
    for x in range(n):
        for y in range(x+1, n):
            if lst.index(x+1) > lst.index(y+1) + delta:
                inversions += 1
                
    return inversions      