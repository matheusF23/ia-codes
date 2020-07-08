"""
Objetivo: maximizar a função f(x)
f(x) = 15x - x^2
x: 0 ... 15
-20*math.exp(-0.2*math.sqrt((1/2)*x**2))-math.exp((1/2)*(math.cos(2*math.pi*x)))+20+math.exp(1)
"""

import random
import math
from matplotlib import pyplot as plt


def convert_to_float(chromosome):
    decimal = 0
    chromosome = chromosome[::-1]
    length = len(chromosome)
    for i in range(length):
        if chromosome[i] == 1:
            decimal = decimal + 2**i

    float_point = -3 + 6*(decimal/((2**8) - 1))

    return float_point


def fitness_function(x):
    return 2*x*math.cos(x**2)
    # return -20*math.exp(-0.2*math.sqrt((1/2)*x**2))-math.exp((1/2)*(math.cos(2*math.pi*x)))+20+math.exp(1)


def create_population(population_size):
    population = []
    chromosome = []

    # Criando população inicial
    while(len(population) != population_size):
        for i in range(8):
            chromosome.append(random.randint(0, 1))

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


def genetic_algorithm(population_size, crossing_rate=0.8, mutation_rate=0.01, generations=100):
    generation = 0
    population = create_population(population_size)
    mean_list = []  # Guardar os valores médios de aptidão da população
    max_list = []   # Guardar os valores da melhor aptidão da população
    generation_list = []    # Guardar o número de gerações
    while(generation < generations):
        fitness = [fitness_function(convert_to_float(chrom))
                   for chrom in population]

        # Seleciona o melhor cromossomo para passar para a próxima geração
        best_chromosome = population[fitness.index(max(fitness))]

        mean = sum(fitness) / len(fitness)
        generation_list.append(generation)
        mean_list.append(mean)
        max_list.append(max(fitness))

        error = max(fitness) - mean
        if(error < 0.00001):
            break

        # É preciso normalizar os valores em fitness entre 0 e 1, para atribuir
        # pesos aos cromossomos na roletaf     .
        fitness_norm = []
        for i in fitness:
            fitness_norm.append((i - min(fitness)) /
                                (max(fitness) - min(fitness)))

        population_with_weight = [
            (population[i],
             int(fitness_norm[i] * 100) + 1) for i in range(population_size)]

        roulette = [chromosome for chromosome,
                    weight in population_with_weight for i in range(weight)]

        parents = []
        while(len(parents) != len(population) // 2):
            father = random.choice(roulette)
            mother = random.choice(roulette)
            # while True:
            #     mother = random.choice(roulette)
            #     if(mother != father):
            #         break
            parents.append((father, mother))

        children = crossing_over(parents, crossing_rate)
        # Adicionar o melhor cromossomo no lugar do pior
        fitness_child = [fitness_function(convert_to_float(chrom))
                         for chrom in children]
        if(min(fitness_child) < max(fitness)):
            children[fitness_child.index(min(fitness_child))] = best_chromosome

        mutation(children, mutation_rate)
        population = children[:]
        generation += 1

    best_x = convert_to_float(best_chromosome)
    plt.figure(num="Aptidão média e melhor aptidão da população")
    plt.plot(generation_list, mean_list, generation_list, max_list)
    plt.title('Aptidão média (azul) e melhor aptidão (laranja) da população')
    plt.ylabel('Aptidão')
    plt.xlabel('Geração')

    plt.show()
    return (f'Melhor valor de x: {best_x}',
            f'f(x) = {max(fitness)}',
            f'Quantidade de gerações: {generation}')


# crossing_rate = float(input("Informe a taxa de cruzamento (entre 0 e 1): "))
# mutation_rate = float(input("Informe a taxa de mutação (entre 0 e 1): "))
population_size = int(input("Informe o tamanho da população: "))
# # generations = int(input("Informe a quantidade de gerações: "))

# , crossing_rate, mutation_rate, generations))
print()
for i in genetic_algorithm(population_size):
    print(i)
