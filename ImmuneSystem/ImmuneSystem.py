import numpy as np

def initialize_population(population_size, dimension):
    """Inicializa una población de soluciones candidatas aleatorias."""
    return np.random.rand(population_size, dimension)

def evaluate_fitness(solution):
    """Evalúa la aptitud de una solución candidata. 
    Este ejemplo utiliza la función esférica simple."""
    return np.sum(solution**2)

def select_antibodies(population, num_antibodies):
    """Selecciona los anticuerpos más aptos de la población."""
    sorted_indices = np.argsort([evaluate_fitness(solution) for solution in population])
    return population[sorted_indices[:num_antibodies]]

def mutate_antibodies(antibodies, mutation_rate):
    """Aplica una mutación a los anticuerpos."""
    mutated_antibodies = antibodies + mutation_rate * np.random.randn(*antibodies.shape)
    return mutated_antibodies

def immune_algorithm(population_size, dimension, num_generations, num_antibodies, mutation_rate):
    """Implementa el algoritmo de sistemas inmunes."""
    population = initialize_population(population_size, dimension)

    for generation in range(num_generations):
        antibodies = select_antibodies(population, num_antibodies)
        mutated_antibodies = mutate_antibodies(antibodies, mutation_rate)

        # Reemplaza las peores soluciones de la población con los anticuerpos mutados
        population[np.argsort([evaluate_fitness(solution) for solution in population])[:num_antibodies]] = mutated_antibodies

        # Imprime la mejor solución en cada generación
        best_solution = population[np.argmin([evaluate_fitness(solution) for solution in population])]
        print(f"Generación {generation + 1}: Mejor solución - {best_solution}, Aptitud - {evaluate_fitness(best_solution)}")

    return population

# Parámetros del algoritmo
population_size = 100
dimension = 5
num_generations = 50
num_antibodies = 10
mutation_rate = 0.1

# Ejecutar el algoritmo de sistemas inmunes
final_population = immune_algorithm(population_size, dimension, num_generations, num_antibodies, mutation_rate)