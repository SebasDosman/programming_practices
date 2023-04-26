import random

def generate_population(size):
    population = []
    
    print("Generating population...")
    
    for i in range(size):
        chromosome = [random.randint(0, 5) for _ in range(6)]
        population.append(chromosome)
        
        print("Chromosome generated: ", chromosome)
    print("")
    
    return population

def evaluate_fitness_percentage(chromosome):
    clashes = 0
    diagonally1, diagonally2 = [0] * ((2 * len(chromosome)) - 1), [0] * ((2 * len(chromosome)) - 1)
    
    for i in range(len(chromosome)):
        diagonally1[i + chromosome[i]] += 1
        diagonally2[len(chromosome) - 1 - i + chromosome[i]] += 1
        
        # for j in range(i + 1, len(chromosome)):
        #     if chromosome[j] == chromosome[i]:
        #         clashes += 1
    
    for j in range((2 * len(chromosome)) - 1):
        if diagonally1[j] > 1:
            clashes += diagonally1[j] - 1
        if diagonally2[j] > 1:
            clashes += diagonally2[j] - 1
    
    return 1 / (clashes + 1)

def evaluate_fitness_integer(chromosome):
    clashes = 0
    diagonally1, diagonally2 = [0] * ((2 * len(chromosome)) - 1), [0] * ((2 * len(chromosome)) - 1)
    
    for i in range(len(chromosome)):
        diagonally1[i + chromosome[i]] += 1
        diagonally2[len(chromosome) - 1 - i + chromosome[i]] += 1
    
    for j in range((2 * len(chromosome)) - 1):
        if diagonally1[j] > 1:
            clashes += diagonally1[j] - 1
        if diagonally2[j] > 1:
            clashes += diagonally2[j] - 1
    
    return clashes

def select_elites(population, num_elites):
    population.sort(key = evaluate_fitness_percentage, reverse = True)
    elites = population[:num_elites]
    
    return elites

def crossover(chromosome1, chromosome2):
    point = random.randint(0, len(chromosome1) - 1)
    
    first_crossover = chromosome1[:point] + chromosome2[point:]
    second_crossover = chromosome2[:point] + chromosome1[point:]
    
    return first_crossover, second_crossover

def mutate(chromosome):
    first_mutation, second_mutation = random.sample(range(len(chromosome)), 2)
    chromosome[first_mutation], chromosome[second_mutation] = chromosome[second_mutation], chromosome[first_mutation]
    
    return chromosome

def replace(population, offspring):
    offspring.sort(key = evaluate_fitness_percentage, reverse = True)
    population[-len(offspring):] = offspring
    
    return population

def print_chromosome(chromosome):
    for i in range(len(chromosome)):
        print(end = " ")
        
        for j in range(len(chromosome)):
            if chromosome[i] == j:
                print("⚫", end = " ")
            else:
                print("⚪", end = " ")
        
        print()

def print_elites(elites):
    for i in range(len(elites)):
        print("Chromosome: ", elites[i])
        print("Fitness: ", evaluate_fitness_integer(elites[i]))
        
        print_chromosome(elites[i])
        print()

def main():
    population = generate_population(100)

    while True:
        elites = select_elites(population, 20)
        print_elites(elites)
        
        offspring = []
        
        for i in range(60):
            parent1, parent2 = random.sample(elites, 2)
            child1, child2 = crossover(parent1, parent2)
            
            child1 = mutate(child1)
            child2 = mutate(child2)
            
            offspring.append(child1)
            offspring.append(child2)
        
        population = replace(population, offspring)
        best_fitness_percentage = evaluate_fitness_percentage(elites[0])
        best_fitness_integer = evaluate_fitness_integer(elites[0])
        
        if best_fitness_percentage == 1:
            print("\n A solution was found!")
            print("Chromosome: ", elites[0])
            
            print_chromosome(elites[0])
            
            break
        
        print("Solution not found yet. Best fitness: ", best_fitness_integer)