#Algoritmo por el método de Búsqueda en profundidad en un grafo (DFS)

#Función por el método DFS
def dfs_grafo(grafo, inicio, visited=None):
    if visited is None:
        visited = set()
    visited.add(inicio)
    for vecino in grafo[inicio]:
        if vecino not in visited:
            dfs_grafo(grafo, vecino, visited)
    
    return visited



grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(dfs_grafo(grafo, 'A'))