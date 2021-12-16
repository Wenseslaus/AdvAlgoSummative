# Input instructions
n = [0, 1, 2, 3, 4, 5]
edges = {(0, 1): 5, (0, 2): 4, (0, 3): 8, (1,3): 3, (1,4): 8, (2, 3): 7, (3, 5): 2}
s = 0

#shortestReach function
def shortestReach(n, edges, s):
    path_lengths = {v: float('inf') for v in n} # Setting infinity to all the far edges
    path_lengths[s] = 0 # Starting path

    adjacent_nodes = {v: {} for v in n} # Adjusting the nodes
    for (u, v), vertix_weight in edges.items(): # Look through each node and 

        adjacent_nodes[u][v] = vertix_weight # Make the new nodes the current vertix weight
        adjacent_nodes[v][u] = vertix_weight # Make the reverse nodes the current weight

    temp_node = [v for v in n] # Assign temp_node as the current looping value
    while len(temp_node) > 0: # Loop to check that the temp node is not less than 0

        upper_bounds = {v: path_lengths[v] for v in temp_node} # Declare the upper bound to hold the 
        u = min(upper_bounds, key=upper_bounds.get) # Find the minimum on th eupper bound

        temp_node.remove(u) # Then relax/release it from the temp node

        for v, vertix_weight in adjacent_nodes[u].items(): # Loop through the adjacent nodes
            path_lengths[v] = min(path_lengths[v], path_lengths[u] + vertix_weight) # assign path lengths to the minimum values

    return path_lengths # Return the path with respective weights.


print(shortestReach(n, edges, s=0))