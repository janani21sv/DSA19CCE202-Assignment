# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
#import sys
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node, distance in enumerate(dist):
            print(node, "\t\t ", distance)

    def minDistance(self, dist, sptSet):
        min_val = float('inf')
        min_index = -1

        for u in range(self.V):
            if dist[u] < min_val and not sptSet[u]:
                min_val = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True

            for y in range(self.V):
                if not sptSet[y] and self.graph[x][y] > 0:
                    dist[y] = min(dist[y], dist[x] + self.graph[x][y])
        self.printSolution(dist)

# Test Case 01
"""g1 = Graph(5)
g1.graph = [
    [0, 3, 0, 7, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 1, 5],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0],
]"""
""""g1.dijkstra(0)"""
"""print()"""

# Test Case 02
"""g2= Graph(4)
g2.graph = [
    [0, 2, 0, 0],
    [0, 0, 1, 3],
    [0, 0, 0, 5],
    [0, 0, 0, 0],
]"""
"""g2.dijkstra(3)"""
"""print()"""

# Test Case 03
g3 = Graph(6)
g3.graph = [
    [0, 1, 0, 3, 0, 0],
    [0, 0, 2, 0, 0, 0],
    [0, 0, 0, 1, 4, 0],
    [0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0],
]
g3.dijkstra(1)

