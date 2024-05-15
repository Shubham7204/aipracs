import random


def hill_climbing(f, generate_neighbors, x, max_iter=100):
    for _ in range(max_iter):
        neighbors = generate_neighbors(x)
        best_neighbor = max(neighbors, key=f)
        if f(best_neighbor) <= f(x):
            return x
        x = best_neighbor
    return x


def objective_function(x):
    return -x ** 2


def generate_neighbors(x):
    return [x + random.uniform(-0.5, 0.5) for _ in range(5)]


initial_solution = 2.0

result = hill_climbing(
    objective_function, generate_neighbors, initial_solution)

print("Optimal solution:", result)
print("Objective value at optimal solution:", objective_function(result))
