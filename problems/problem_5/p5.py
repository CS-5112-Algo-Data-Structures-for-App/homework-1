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
    
    # Creates a list of links with the following format (origin,destination,distance)
    links = []
    for origin_apt in apartments:
        for destination_apt in apartments:
            if origin_apt != destination_apt:
                links.append((origin_apt,destination_apt, calculate_manhattan_distance(origin_apt,destination_apt)))
    
    # Sort links by distance low to high
    links.sort(key = lambda link: link[2])
    
    mst = []
    visited_nodes = set()
    
    # Go through each link
    for link in links:
        origin_node = link[0]
        destination_node = link[1]
        
        # Check if cycle
        if origin_node not in visited_nodes or destination_node not in visited_nodes:
            mst.append((origin_node,destination_node))
            visited_nodes.add(origin_node) #
            visited_nodes.add(destination_node)
    

    # for edge
    # # If the two vertices are not already in the spanning tree, add the edge to the spanning tree.
    # if vertex1 not in mst_vertices or vertex2 not in mst_vertices:
    #     mst_edges.append(edge)
    #     mst_vertices.add(vertex1)
    #     mst_vertices.add(vertex2)

    return mst
    




print(cookies_distrubution_map([(1,4), (5, 1), (5, 5), (5, 4), (3, 2), (6, 4)]))

# ans 
# ((1,1), (3, 2)),
# ((3,2), (5,1)), 
# ((1,1), (1,4)),
# ((5,4), (5,5)), 
# ((5,4), (6,4)),
# ((5,1), (5,4))