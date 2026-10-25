
# A* Search Algorithm

import heapq


def a_star(graph, heuristic, start, goal):

    # Priority queue: (f_cost, g_cost, node, path)
    pq = [(heuristic[start], 0, start, [start])]

    visited = {}

    while pq:

        f_cost, g_cost, node, path = heapq.heappop(pq)

        # Skip if a better path was already found
        if node in visited and visited[node] <= g_cost:
            continue

        visited[node] = g_cost

        # Goal test
        if node == goal:
            return path, g_cost

        # Explore neighbors
        for neighbor, cost in graph.get(node, []):

            new_g = g_cost + cost
            new_f = new_g + heuristic[neighbor]

            heapq.heappush(
                pq,
                (
                    new_f,
                    new_g,
                    neighbor,
                    path + [neighbor]
                )
            )

    return None, float("inf")


# Main program
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 5)],
    'E': [('G', 2)],
    'F': [('G', 3)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 2,
    'G': 0
}

start = input("Enter start node: ").upper()
goal = input("Enter goal node: ").upper()

path, cost = a_star(graph, heuristic, start, goal)

if path:
    print("Optimal path:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("Goal not reachable")
