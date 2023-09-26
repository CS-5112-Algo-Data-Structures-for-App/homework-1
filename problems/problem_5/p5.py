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

    # make a MST and return it in the format [((1,1), (1,2)), ((1,1), (2,1))
    # keep a visited set and add the first point to it
    # while the visited set is not equal to the number of points in the graph
    # iterate through the points in the visited set and find the next point that is closest to it
    # add that point to the visited set and add the edge to the MST
    visited = set()
    visited.add(apartments[0])
    mst = []
    while len(visited) != len(apartments):
        closest_point = None
        closest_distance = float('inf')
        for point in visited:
            for edge in map[point]:
                if edge[0] not in visited and edge[1] < closest_distance:
                    closest_point = edge[0]
                    closest_distance = edge[1]
        visited.add(closest_point)
        mst.append((closest_point, closest_distance))
    return mst
        
    




print(cookies_distrubution_map([(1,4), (5, 1), (5, 5), (5, 4), (3, 2), (6, 4)]))

# ans 
# ((1,1), (3, 2)),
# ((3,2), (5,1)), 
# ((1,1), (1,4)), 
# ((5,4), (5,5)), 
# ((5,4), (6,4)), #
# ((5,1), (5,4))
