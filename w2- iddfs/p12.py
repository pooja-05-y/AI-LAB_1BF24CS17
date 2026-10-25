
# Iterative Deepening Search (IDS)

def depth_limited_search(graph, node, goal, depth, path):

    path.append(node)

    if node == goal:
        return path.copy()

    if depth == 0:
        path.pop()
        return None

    for neighbor in graph.get(node, []):

        if neighbor not in path:

            result = depth_limited_search(
                graph, neighbor, goal, depth - 1, path
            )

            if result is not None:
                return result

    path.pop()
    return None


def iterative_deepening_search(graph, start, goal):

    max_depth = 0

    while True:

        path = []

        result = depth_limited_search(
            graph, start, goal, max_depth, path
        )

        if result is not None:
            return result

        max_depth += 1


# Main program
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

start = input("Enter start node: ").upper()
goal = input("Enter goal node: ").upper()

result = iterative_deepening_search(graph, start, goal)

if result:
    print("Goal found!")
    print("Path:", " -> ".join(result))
else:
    print("Goal not found")
