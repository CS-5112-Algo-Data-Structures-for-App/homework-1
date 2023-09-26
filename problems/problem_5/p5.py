'''
Problem 5

input: List of tuples representing the friend's apartments.
output: List of apartment pairs.

TODO: implement your solution.
'''
def calculate_manhattan_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def cookies_distrubution_map(apartments) -> list:
    #using all the points in the graph create a map of all the points and their distances from each other
    #for each point in the graph, calculate the distance to all other points and store it in a map
    #the map should be of the form {(x,y): [(x1,y1, distance), (x2,y2, distance)]}
    #for each point in the graph, calculate the distance to all other points and store it in a map
    #the map should be of the form {(x,y): [(x1,y1, distance), (x2,y2, distance)]}
    map = {}
    for i in range(len(apartments)):
        for j in range(len(apartments)):
            if i != j:
                distance = calculate_manhattan_distance(apartments[i], apartments[j])
                if apartments[i] not in map:
                    map[apartments[i]] = [(apartments[j], distance)]
                else:
                    map[apartments[i]].append((apartments[j], distance))

    # make a MST and return it in the format [((1,1), (1,2)), ((1,1), (2,1))
    
    return []
