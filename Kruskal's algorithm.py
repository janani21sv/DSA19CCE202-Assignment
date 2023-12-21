def kruskal(graph):
    edges = [(weight, u, v) for u, neighbors in graph.items() for v, weight in neighbors.items()]
    edges.sort()

    parent = {node: node for node in graph}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(u, v):
        root_u, root_v = find(u), find(v)
        parent[root_u] = root_v

    mst = []
    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((weight, u, v))

    return mst

# Sample case 01
graph_example_1 = {
    'A': {'B': 2, 'D': 1},
    'B': {'A': 2, 'C': 3, 'D': 2},
    'C': {'B': 3, 'D': 4},
    'D': {'A': 1, 'B': 2, 'C': 4}
}

result_1 = kruskal(graph_example_1)
print("Minimum Spanning Tree(Kruskal's Algorithm):", result_1)
"""
# Sample case 02
graph_example_2 = {
    'A': {'B': 3, 'C': 1},
    'B': {'A': 3, 'C': 4, 'D': 2},
    'C': {'A': 1, 'B': 4, 'D': 5},
    'D': {'B': 2, 'C': 5}
}

result_2 = kruskal(graph_example_2)
print("\nMinimum Spanning Tree(Kruskal's Algorithm):", result_2)

# Sample case 03
graph_example_3 = {
    'X': {'Y': 2, 'Z': 3},
    'Y': {'X': 2, 'Z': 4},
    'Z': {'X': 3, 'Y': 4}
}

result_3 = kruskal(graph_example_3)
print("\nMinimum Spanning Tree - Example 3 (Kruskal's Algorithm):", result_3)
"""
