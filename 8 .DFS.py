def dfs(graph, start):
    visited = [False] * len(graph)
    stack = [start]
    traversal_order = []
    total_cost = 0
    
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            traversal_order.append(vertex)
            for neighbor, cost in enumerate(graph[vertex]):
                if cost > 0 and not visited[neighbor]:
                    stack.append(neighbor)
                    total_cost += cost
    
    return traversal_order, total_cost

# Example graph represented by an adjacency matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_vertex = 0  # Starting vertex for DFS
traversal_order, total_cost = dfs(graph, start_vertex)

# Print traversal order and total cost
print("Traversal Order:", traversal_order)
print("Total Cost:", total_cost)
 
# Visualization of traversal
print("Graph Traversal:")
for i in range(len(graph)):
    row_str = " -> ".join(["{:<3}".format(graph[i][j]) for j in range(len(graph[i]))])
    print(row_str)

# Display traversal path
print("\nTraversal Path:")
for i in range(len(traversal_order) - 1):
    print(f"{traversal_order[i]} -> ", end="")
print(traversal_order[-1])
