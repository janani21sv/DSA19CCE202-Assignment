class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight): 
        self.edges.append((u, v, weight))

    def bellman_ford(self, source): 
        distances = {vertex: float('inf') for vertex in range(self.vertices)}
        predecessors = {vertex: None for vertex in range(self.vertices)}
        distances[source] = 0

       
        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

        
        for u, v, weight in self.edges:
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative cycle")
        return distances, predecessors


# Sample case 01
print("Test Case 1:")
g1 = Graph(5)
g1.add_edge(0, 1, 6)
g1.add_edge(0, 3, 7)
g1.add_edge(1, 2, 5)
g1.add_edge(1, 3, 8)
g1.add_edge(1, 4, -4)
g1.add_edge(2, 1, -2)
g1.add_edge(3, 2, -3)
g1.add_edge(3, 4, 9)
g1.add_edge(4, 0, 2)
g1.add_edge(4, 2, 7)
source_vertex_1 = 3
distances_1, predecessors_1 = g1.bellman_ford(source_vertex_1)
print("Shortest distances from source vertex", source_vertex_1)
for vertex in range(g1.vertices):
    print(f"Vertex {vertex}: Distance = {distances_1[vertex]}, Predecessor = {predecessors_1[vertex]}")
print()
"""
# Sample case 02
print("Test Case 2:")
g2 = Graph(5)
g2.add_edge(0, 1, 6)
g2.add_edge(0, 3, 7)
g2.add_edge(1, 2, 5)
g2.add_edge(1, 3, 8)
g2.add_edge(1, 4, -4)
g2.add_edge(2, 1, -2)
g2.add_edge(3, 2, -3)
g2.add_edge(3, 4, 9)
g2.add_edge(4, 0, 2)
g2.add_edge(4, 2, 7)
source_vertex_2 = 0
distances_2, predecessors_2 = g2.bellman_ford(source_vertex_2)
print("Shortest distances from source vertex", source_vertex_2)
for vertex in range(g2.vertices):
    print(f"Vertex {vertex}: Distance = {distances_2[vertex]}, Predecessor = {predecessors_2[vertex]}")
print()

# Sample case 03
print("Test Case 3:")
g3 = Graph(5)
g3.add_edge(0, 1, 6)
g3.add_edge(0, 3, 7)
g3.add_edge(1, 2, 5)
g3.add_edge(1, 3, 8)
g3.add_edge(1, 4, -4)
g3.add_edge(2, 1, -2)
g3.add_edge(3, 2, -3)
g3.add_edge(3, 4, 9)
g3.add_edge(4, 0, 2)
g3.add_edge(4, 2, 7)
source_vertex_3 = 1
distances_3, predecessors_3 = g3.bellman_ford(source_vertex_3)
print("Shortest distances from source vertex", source_vertex_3)
for vertex in range(g3.vertices):
    print(f"Vertex {vertex}: Distance = {distances_3[vertex]}, Predecessor = {predecessors_3[vertex]}")
print()
"""