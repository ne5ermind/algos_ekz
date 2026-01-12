class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def add_edge(self, x, y, weight=1):
        if 0 <= x < self.num_nodes and 0 <= y < self.num_nodes:
            self.matrix[x][y] = weight
            self.matrix[y][x] = weight
        else:
            raise IndexError("Node out of range")

    def remove_edge(self, x, y):
        self.add_edge(x, y, 0)

    def print(self):
        for i in self.matrix:
            print(" ".join(map(str, i)))


# %%

graph = Graph(6)

graph.add_edge(1, 2, 3)
graph.add_edge(4, 5, 6)
graph.add_edge(1, 4, 1)
graph.add_edge(3, 5)

graph.print()

print("\n")
graph.remove_edge(3, 5)

graph.print()
# %%
