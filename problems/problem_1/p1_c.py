'''
Problem 1c

input: File containing an integer n followed by 2n lines containing the preferences of the n students and then the n hospitals (see README).
output: Dictionary mapping students to hospitals. 

TODO: Implement the Gale-Shapley algorithm to run in O(n^2).
'''
def stable_matching_1c(file) -> dict:
    n = 0
    doctors_pref = []
    hospitals_pref = []

    with open(file, "r") as f:
        n = int(f.readline())
        for _ in range(n):
            d_pref = f.readline().split()
            doctors_pref.append([int(x) for x in d_pref])

        for _ in range(n):
            h_pref = f.readline().split()
            hospitals_pref.append([int(x) for x in h_pref])
    
    # doctors to hospitals map
    pairs = {} 
    
    
        

    return pairs