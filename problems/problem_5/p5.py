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

    visited_nodes = set()
    visited_nodes.add(apartments[0])
    mst = []
    while len(visited_nodes) < len(apartments):
        best_link = (None,None,float('inf'))
        for origin_node in visited_nodes:
            for link in apartments_dict[origin_node]:
                if link[0] not in visited_nodes and link[1] < best_link[2]:
                    best_link = (origin_node,link[0],link[1])
        visited_nodes.add(best_link[1])
        mst.append((best_link[0],best_link[1]))
    return mst
    