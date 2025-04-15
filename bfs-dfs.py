def bfs(graph, start):
    visited = []         # Liste des nœuds visités
    queue = [start]      # File pour explorer
   
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex])
    
    return visited

def dfs(graph, start):
    visited = []         # Liste des nœuds visités
    stack = [start]      # File pour explorer
   
    while stack:
        vertex = stack.pop(-1)  # Pop last element for DFS
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(graph[vertex])
    
    return visited

# in dfs : just chenge queue to stack, and pop last element like vertex = queue.pop(-1)

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
    
    
print()
for key in i:
    print(f"DFS starting from {key}: {dfs(graph, key)}")