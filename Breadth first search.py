from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# sample case 01
graph_example5 = {
    'X': ['Y', 'Z'],
    'Y': ['X', 'W'],
    'Z': ['X', 'W'],
    'W': ['Y', 'Z']
}
bfs(graph_example5, 'X')

# sample case 02
"""graph_example6 = {
    10: [20, 30, 40],
    20: [10, 50],
    30: [10, 60],
    40: [10],
    50: [20],
    60: [30]
}
bfs(graph_example6, 10)"""

# sample case 03
"""graph_example7 = {
    'Red': ['Green', 'Blue'],
    'Green': ['Red', 'Yellow'],
    'Blue': ['Red', 'Yellow'],
    'Yellow': ['Green', 'Blue']
}
bfs(graph_example7, 'Red')"""
