from collections import defaultdict

def build_graph():
    graph = defaultdict(dict)
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))
    print("Enter edges (u v weight):")
    for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w 
    return graph

def get_heuristics(n):
    h = {}
    print("Enter heuristic values for each vertex:")
    for i in range(n):
        h[i] = int(input(f"Heuristic for {i}: ")) 
    return h

def a_star(graph, start, goal, h): 
    open_set = [(h[start], start)] 
    came_from = {} 
    g_score = {node: float('inf') for node in graph} 
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph} 
    f_score[start] = h[start]

    while open_set:
        open_set.sort()
        current_f, current = open_set.pop(0)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor, weight in graph[current].items():
            tentative_g = g_score[current] + weight
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + h[neighbor]
                if neighbor not in [item[1] for item in open_set]:
                    open_set.append((f_score[neighbor], neighbor))

    return None

if __name__ == "__main__":
    graph = build_graph()
    n = len(graph)
    h = get_heuristics(n)
    start = int(input("Enter start vertex: "))
    goal = int(input("Enter goal vertex: "))
    path = a_star(graph, start, goal, h)
    if path:
        print("Shortest path:", path)
    else:
        print("No path found")
