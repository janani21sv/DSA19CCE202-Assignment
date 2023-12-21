visited_nodes = set()

def dfs_traversal(graph, start_node):
    if start_node not in visited_nodes:
        print(start_node)
        visited_nodes.add(start_node)
        for neighbor in graph[start_node]:
            dfs_traversal(graph, neighbor)

# Sample case 01
graph_example_1 = {
    'X': ['Y', 'Z'],
    'Y': ['W'],
    'Z': [],
    'W': ['V'],
    'V': []
}
print("DFS Traversal - Example 1:")
visited_nodes.clear()
dfs_traversal(graph_example_1, 'X')

# Sample case 02
"""graph_example_2 = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [6],
    5: [],
    6: []
}
print("\nDFS Traversal - Example 2:")
visited_nodes.clear()
dfs_traversal(graph_example_2, 1)"""

# Sample case 03
"""graph_example_3 = {
    'Red': ['Green', 'Blue'],
    'Green': ['Yellow'],
    'Blue': [],
    'Yellow': ['Orange'],
    'Orange': []
}
print("\nDFS Traversal - Example 3:")
visited_nodes.clear()
dfs_traversal(graph_example_3, 'Red')"""
