import numpy as np
import matplotlib.pyplot as plt

def generate_random_solution(num_cities):
    """Generate a random solution for the TSP problem."""
    return np.random.permutation(num_cities)

def calculate_total_distance(solution, distances):
    """Calculate the total distance of a TSP solution."""
    total_distance = 0
    num_cities = len(solution)
    for i in range(num_cities - 1):
        total_distance += distances[solution[i], solution[i + 1]]
    total_distance += distances[solution[-1], solution[0]]  # Return to the starting city
    return total_distance

def simulated_annealing(distances, initial_temperature=1000, cooling_rate=0.95, num_iterations=1000):
    num_cities = len(distances)
    current_solution = generate_random_solution(num_cities)
    current_distance = calculate_total_distance(current_solution, distances)

    best_solution = current_solution.copy()
    best_distance = current_distance

    temperature = initial_temperature

    for iteration in range(num_iterations):
        # Generate a new candidate solution by swapping two random cities
        new_solution = current_solution.copy()
        indices = np.random.choice(num_cities, size=2, replace=False)
        new_solution[indices[0]], new_solution[indices[1]] = new_solution[indices[1]], new_solution[indices[0]]
        new_distance = calculate_total_distance(new_solution, distances)

        # Accept the new solution if it is better or with a certain probability
        if new_distance < current_distance or np.random.rand() < np.exp((current_distance - new_distance) / temperature):
            current_solution = new_solution
            current_distance = new_distance

        # Update the best solution if necessary
        if current_distance < best_distance:
            best_solution = current_solution.copy()
            best_distance = current_distance

        # Cool down the temperature
        temperature *= cooling_rate

    return best_solution, best_distance

# Example usage:
if __name__ == "__main__":
    # Example distance matrix (replace this with your own data)
    distances = np.array([
        [0, 2, 3, 1],
        [2, 0, 4, 2],
        [3, 4, 0, 3],
        [1, 2, 3, 0]
    ])

    # Parameters
    initial_temperature = 1000
    cooling_rate = 0.95
    num_iterations = 1000

    # Run Simulated Annealing algorithm
    best_solution, best_distance = simulated_annealing(distances, initial_temperature, cooling_rate, num_iterations)

    # Print the results
    print("Best Solution:", best_solution)
    print("Best Distance:", best_distance)

    # Plot the best solution
    plt.figure(figsize=(8, 6))
    plt.plot(distances[best_solution, 0], distances[best_solution, 1], marker='o', linestyle='-')
    plt.title("Best TSP Solution found by Simulated Annealing")
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.show()
    