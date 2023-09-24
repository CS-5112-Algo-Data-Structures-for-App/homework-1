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
    unmatched_hospitals = list(range(n))
    
    while len(unmatched_hospitals) > 0: # continue looping if some hospitals are unmatched
        
        for hospital in unmatched_hospitals: # only loop through the unmatched hospitals
            for doctor in hospitals_pref[hospital]:
                
                if doctor not in pairs.keys(): # doctor does not have a match
                    pairs[doctor] = hospital
                    unmatched_hospitals.remove(hospital)
                    break
                else: # doctor has already been matched to an existing hospital
                    if doctors_pref[doctor].index(hospital) < doctors_pref[doctor].index(pairs[doctor]):
                        hospitals_pref[pairs[doctor]].remove(doctor) # remove doctor from list so it is not relooped over
                        
                        unmatched_hospitals.remove(hospital)
                        pairs[doctor] = hospital
                        break
                


    return pairs

# print(stable_matching_1c(r'test_p1_student_n10.txt'))