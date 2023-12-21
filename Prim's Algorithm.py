INF = float('inf')

def print_mst_result(selected, parent, graph):
    print("Edge : Weight")
    for i in range(1, len(graph)):
        print(f"{parent[i]} - {i}: {graph[i][parent[i]]}")

def prim_mst(graph):
    V = len(graph)
    selected = [False] * V
    parent = [None] * V

    selected[0] = True
    no_edge = 0

    while no_edge < V - 1:
        minimum = INF
        x = 0
        y = 0

        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if (not selected[j]) and graph[i][j] and minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j

        parent[y] = x
        selected[y] = True
        no_edge += 1

    print_mst_result(selected, parent, graph)

# Sample case 01
graph_example_1 = [
    [0, 1, 3, 0, 1],
    [1, 0, 2, 5, 4],
    [3, 2, 0, 4, 7],
    [0, 5, 4, 0, 9],
    [0, 5, 7, 9, 0]
]

print("Minimum Spanning Tree:")
prim_mst(graph_example_1)

# Sample case 02
"""graph_example_2 = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

print("\nMinimum Spanning Tree:")
prim_mst(graph_example_2)"""

#  Sample case 03
"""graph_example_3 = [
    [0, 1, 3, 0, 1],
    [1, 0, 2, 5, 4],
    [3, 2, 0, 4, 7],
    [0, 5, 4, 0, 9],
    [0, 5, 7, 9, 0]
]

print("\nMinimum Spanning Tree:")
prim_mst(graph_example_3)"""
