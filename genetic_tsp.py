import numpy as np
import random

# Define the distance matrix
distance_matrix = {
    'A': {'A': 0, 'B': 16, 'C': 11, 'D': 6},
    'B': {'A': 8, 'B': 0, 'C': 13, 'D': 16},
    'C': {'A': 4, 'B': 7, 'C': 0, 'D': 9},
    'D': {'A': 5, 'B': 12, 'C': 2, 'D': 0}
}

# Define the cities
cities = list(distance_matrix.keys())

# Define the parameters for the genetic algorithm
population_size = 50
mutation_rate = 0.01
num_generations = 1000

# Function to calculate the total distance of a route


def total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += distance_matrix[route[i]][route[i + 1]]
    # Return to the starting city
    total += distance_matrix[route[-1]][route[0]]
    return total

# Function to generate an initial population


def initial_population(population_size):
    population = []
    for _ in range(population_size):
        route = cities.copy()
        random.shuffle(route)
        population.append(route)
    return population

# Function to perform crossover


def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child = parent1[:crossover_point]
    for city in parent2:
        if city not in child:
            child.append(city)
    return child

# Function to perform mutation


def mutate(route, mutation_rate):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route

# Function to select parents for crossover


def selection(population):
    fitness_values = [1 / total_distance(route) for route in population]
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    return random.choices(population, weights=probabilities, k=2)

# Main genetic algorithm function


def genetic_algorithm(population_size, mutation_rate, num_generations):
    population = initial_population(population_size)
    for generation in range(num_generations):
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = selection(population)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population
        best_route = min(population, key=total_distance)
        best_distance = total_distance(best_route)
        fitness_values = [1 / total_distance(route) for route in population]
        average_fitness = sum(fitness_values) / len(fitness_values)
        print(
            f"Generation {generation + 1}: Best Route - {best_route}, Total Distance - {best_distance}, Average Fitness - {average_fitness}")
    return min(population, key=total_distance), total_distance(min(population, key=total_distance))


# Run the genetic algorithm
best_route, best_distance = genetic_algorithm(
    population_size, mutation_rate, num_generations)
print(f"\nBest Route: {best_route}, Total Distance: {best_distance}")