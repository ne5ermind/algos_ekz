class Graph:
    def __init__(self, directed=False):
        self._adj_list = {}
        self._directed = directed

    def add_node(self, node):
        if node not in self._adj_list:
            self._adj_list[node] = set()

    def add_edge(self, x, y):
        self.add_node(x)
        self.add_node(y)

        self._adj_list[x].add(y)
        if not self._directed:
            self._adj_list[y].add(x)

    def remove_edge(self, x, y):
        if x in self._adj_list:
            self._adj_list[x].discard(y)
        if not self._directed and y in self._adj_list:
            self._adj_list[y].discard(x)

    def get_nodes(self):
        return list(self._adj_list.keys())

    def get_neighbors(self, x):
        return self._adj_list[x]

    def __str__(self):
        return "\n".join([f"{node}: {neig}" for node, neig in self._adj_list.items()])


# %%

graph = Graph()

graph.add_node("A")
graph.add_edge("A", "M")
graph.add_edge("O", "G")
graph.add_edge("U", "S")

print(graph.get_neighbors("A"))
print(graph.get_nodes())

graph.add_edge("A", "G")
graph.add_edge("A", "S")
graph.add_edge("A", "I")

print(graph)

graph.remove_edge("A", "S")

print(graph)
# %%
