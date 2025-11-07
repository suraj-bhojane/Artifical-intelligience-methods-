import heapq

def prim_mst(graph, start):
    visited = set()
    min_heap = [(0, start, -1)]  # (weight, vertex, parent)
    total_weight = 0
    mst_edges = []

    while min_heap:
        weight, vertex, parent = heapq.heappop(min_heap)
        if vertex in visited:
            continue
        visited.add(vertex)
        total_weight += weight
        if parent != -1:
            mst_edges.append((parent, vertex, weight))

        for neighbor, w in graph[vertex]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor, vertex))

    print("\nEdges in the Minimum Spanning Tree:")
    for u, v, w in mst_edges:
        print(f"{u} - {v} (weight {w})")
    print("Total cost of MST:", total_weight)


# --- MAIN PROGRAM ---
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(n)}

print("Enter each edge in the format: u v weight")
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # undirected graph

start = int(input(f"Enter the starting vertex (0 to {n-1}): "))

prim_mst(graph, start)
