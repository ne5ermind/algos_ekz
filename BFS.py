from collections import deque


def bfs(graph, start_node):
    visited = list(start_node)
    queue = deque([start_node])
    output = []

    while queue:
        current = queue.popleft()
        output.append(current)

        for n in graph[current]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    return output


# %%

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print(bfs(graph, "A"))
# %%

