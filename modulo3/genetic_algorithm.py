"""
Objetivo: maximizar a função f(x)
f(x) = 15x - x^2
x: 0 ... 15
-20ℯ^(-0.2*sqrt((1)/(2) (x^(2)+y^(2))))-ℯ^((1)/(2) (cos(2π*x)+cos(2π*y)))+20+ℯ^(1)
"""

import random
import math


def convert_to_decimal(chromosome):
    decimal = 0
    chromosome = chromosome[::-1]
    length = len(chromosome)
    for i in range(length):
        if chromosome[i] == 1:
            decimal = decimal + 2**i

    return decimal

def fitness_function(x):
    # return 15*x - x**2
    return -20*math.exp(-0.2*math.sqrt((1/2)*x**2))-math.exp((1/2)*(math.cos(2*math.pi*x)))+20+math.exp(1)


def create_population(population_size):
    population = []
    chromosome = []

    # Criando população inicial
    while(len(population) != population_size):
        for i in range(5):
            chromosome.append(random.randint(0, 1))

        if(chromosome not in population):
            population.append(chromosome)

        chromosome = []

    return population


def crossing_over(parents, crossing_rate):
    children = []
    for parent in parents:
        father = parent[0]
        mother = parent[1]
        rate = random.random()
        if(rate < crossing_rate):
            cut = random.randint(1, len(father) - 1)
            children.append(father[:cut] + mother[cut:])
            children.append(mother[:cut] + father[cut:])
        else:
            children.append(father)
            children.append(mother)

    return children


def mutation(children, mutation_rate):
    for child in children:
        rate = random.random()
        if (rate < mutation_rate):
            position = random.randint(0, len(child) - 1)
            child[position] = 0**child[position]


def genetic_algorithm(population_size, crossing_rate=0.7, mutation_rate=0.01, generations=100):
    generation = 0
    population = create_population(population_size)
    while(generation < generations):
        fitness = [fitness_function(convert_to_decimal(chrom))
                   for chrom in population]

        mean = int(sum(fitness) / len(fitness))
        error = max(fitness) - mean
        if(error < 2):
            for i, v in enumerate(fitness):
                if (v == max(fitness)):
                    return convert_to_decimal(population[i]), generation

        population_with_weight = [(population[i], int(
            (fitness[i] / sum(fitness)) * 100) + 1) for i in range(len(population))]

        roulette = [chromosome for chromosome,
                    weight in population_with_weight for i in range(weight)]

        parents = []
        while(len(parents) != len(population) // 2):
            father = random.choice(roulette)
            while True:
                mother = random.choice(roulette)
                if(mother != father):
                    break
            parents.append((father, mother))

        children = crossing_over(parents, crossing_rate)
        mutation(children, mutation_rate)
        population = children[:]
        generation += 1

    for i, v in enumerate(fitness):
        if (v == max(fitness)):
            return convert_to_decimal(population[i]), generation


# crossing_rate = float(input("Informe a taxa de cruzamento (entre 0 e 1): "))
# mutation_rate = float(input("Informe a taxa de mutação (entre 0 e 1): "))
population_size = int(input("Informe o tamanho da população: "))
# # generations = int(input("Informe a quantidade de gerações: "))

# , crossing_rate, mutation_rate, generations))
print(genetic_algorithm(population_size))
