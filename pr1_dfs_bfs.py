from collections import defaultdict, deque 
def input_graph():
    graph = defaultdict(list) 
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))
    print("Enter edges (u v):")
    for _ in range(e):
        u, v = map(int ,input().split())
        graph[u].append(v)
        graph[v].append(u) 
    return graph

def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited) 

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

if __name__ == "__main__":
    graph = input_graph()
    start =int(input("Enter starting vertex: "))
    print("DFS Traversal:")
    dfs_recursive(graph, start)
    print("\nBFS Traversal:")
    bfs(graph, start)
