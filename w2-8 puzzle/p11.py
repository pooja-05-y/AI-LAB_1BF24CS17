
import heapq

# Goal state
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Calculate Manhattan Distance
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_index = GOAL.index(state[i])

            current_row = i // 3
            current_col = i % 3

            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


# Generate possible neighboring states
def get_neighbors(state):
    neighbors = []

    zero_index = state.index(0)

    row = zero_index // 3
    col = zero_index % 3

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_index = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with neighboring tile
            new_state[zero_index], new_state[new_index] = (
                new_state[new_index],
                new_state[zero_index]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# A* Search Algorithm
def a_star(start):
    priority_queue = []

    # (f_cost, g_cost, state, path)
    heapq.heappush(
        priority_queue,
        (heuristic(start), 0, start, [start])
    )

    visited = set()

    while priority_queue:

        f_cost, g_cost, current, path = heapq.heappop(
            priority_queue
        )

        if current == GOAL:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current):

            if neighbor not in visited:

                new_g = g_cost + 1
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    priority_queue,
                    (
                        new_f,
                        new_g,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None


# Print the puzzle
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()


# Main program
start = tuple(map(
    int,
    input("Enter initial state (9 numbers, use 0 for blank): ").split()
))

if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid input! Enter numbers 0 to 8 exactly once.")

else:
    solution = a_star(start)

    if solution:
        print("\nSolution found!")
        print("Number of moves:", len(solution) - 1)

        for step, state in enumerate(solution):
            print("Step", step)
            print_puzzle(state)

    else:
        print("No solution exists.")
