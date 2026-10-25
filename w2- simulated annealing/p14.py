
# Simulated Annealing Algorithm

import math
import random


# Objective function to maximize
def objective(x):
    return -(x - 3) ** 2 + 10


# Simulated Annealing
def simulated_annealing():

    # Initial solution
    current = random.uniform(-10, 10)

    # Best solution found
    best = current

    # Initial temperature
    temperature = 100

    # Cooling rate
    cooling_rate = 0.95

    # Minimum temperature
    min_temperature = 0.001

    while temperature > min_temperature:

        # Generate a neighboring solution
        neighbor = current + random.uniform(-1, 1)

        # Calculate change in objective value
        delta = objective(neighbor) - objective(current)

        # Accept better solutions
        if delta > 0:
            current = neighbor

        # Sometimes accept worse solutions
        else:
            probability = math.exp(delta / temperature)

            if random.random() < probability:
                current = neighbor

        # Update best solution
        if objective(current) > objective(best):
            best = current

        # Reduce temperature
        temperature *= cooling_rate

    return best


# Main program
best_solution = simulated_annealing()

print("Best solution:", round(best_solution, 4))
print("Maximum value:", round(objective(best_solution), 4))
