def prim_mst(graph, vertices):
    V = len(vertices)
    selected = [False] * V
    selected[0] = True
    edges = []

    print("\nEdges in MST with their weights:")

    for _ in range(V - 1):
        min_edge = 1000000
        a = b = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j]:
                        if graph[i][j] < min_edge:
                            min_edge = graph[i][j]
                            a, b = i, j
        print(f"{vertices[a]} - {vertices[b]}: {graph[a][b]}")
        edges.append((vertices[a], vertices[b], graph[a][b]))
        selected[b] = True

    return edges

# Input vertices as names
V = int(input("Enter number of vertices: "))
vertices = []
for i in range(V):
    name = input(f"Enter name of vertex {i+1}: ")
    vertices.append(name)

# Input edges
E = int(input("Enter number of edges: "))
graph = [[0]*V for _ in range(V)]

print("Enter each edge as: vertex1 vertex2 weight")
for _ in range(E):
    u_name, v_name, w = input().split()
    w = int(w)
    u = vertices.index(u_name)
    v = vertices.index(v_name)
    graph[u][v] = w
    graph[v][u] = w  # undirected graph

mst = prim_mst(graph, vertices)
