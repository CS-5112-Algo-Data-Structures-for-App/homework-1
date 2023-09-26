'''
Problem 5

input: List of tuples representing the friend's apartments.
output: List of apartment pairs.

TODO: implement your solution.
'''
def calculate_manhattan_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def cookies_distrubution_map(apartments) -> list:
    
    # Add in origin node if not already in the set (1,1)
    if (1,1) not in apartments:
        apartments.insert(0,(1,1))
    
    # Set up graph
    apartments_dict = {}
    
    for i in range(len(apartments)):
        for j in range(len(apartments)):
            if i != j:
                distance = calculate_manhattan_distance(apartments[i], apartments[j])
                if apartments[i] not in apartments_dict:
                    apartments_dict[apartments[i]] = [(apartments[j], distance)]
                else:
                    apartments_dict[apartments[i]].append((apartments[j], distance))
    
    links_mst= []
    visited_nodes = set()
    
    visited_nodes.add((1,1))

    
        
    




print(cookies_distrubution_map([(1,4), (5, 1), (5, 5), (5, 4), (3, 2), (6, 4)]))

# ans 
# ((1,1), (3, 2)),
# ((3,2), (5,1)), 
# ((1,1), (1,4)), 
# ((5,4), (5,5)), 
# ((5,4), (6,4)), #
# ((5,1), (5,4))