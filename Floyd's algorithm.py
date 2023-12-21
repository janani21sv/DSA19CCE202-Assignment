def floyd_warshall(graph):
    v = len(graph)
    distance = [[float('inf') for _ in range(v)] for _ in range(v)]
   
    for i in range(v):
        for j in range(v):
            distance[i][j] = graph[i][j]

    for k in range(v):
        for i in range(v):
            for j in range(v):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    print("Shortest distances between every pair of vertices:")
    for row in distance:
        print(' '.join(str(element) if element != float('inf') else 'INF' for element in row))
    print()


# Sample case 01
graph_example1 = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]
floyd_warshall(graph_example1)

#  Sample case 02
"""graph_example2 = [
    [0, 2, float('inf'), 8],
    [float('inf'), 0, 1, float('inf')],
    [float('inf'), float('inf'), 0, 4],
    [float('inf'), float('inf'), float('inf'), 0]
]
floyd_warshall(graph_example2)"""

#  Sample case 03
"""graph_example3 = [
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
]
floyd_warshall(graph_example3)"""
