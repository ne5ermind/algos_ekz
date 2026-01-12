def dfs_recursive(graph, node, visited=list()):
    visited.append(node)

    for n in graph[node]:
        if n not in visited:
            dfs_recursive(graph, n, visited)

    return visited
# %%

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

print(dfs_recursive(graph, "A"))
# %%

