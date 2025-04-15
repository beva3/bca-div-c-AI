def dfs(graph, start):
    visited = []         # Liste des nœuds visités
    stack = [start]      # Pile pour explorer

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))  # On ajoute les voisins (dans l’ordre)

    return visited

def bfs(graph, start):
    visited = []         # Liste des nœuds visités
    queue = [start]      # File pour explorer

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])  # Ajoute les voisins

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

i = list(graph.keys()) 

for key in i:
    print(f"DFS starting from {key}: {bfs(graph, key)}")
    
for key in i:
    print(f"DFS starting from {key}: {dfs(graph, key)}")