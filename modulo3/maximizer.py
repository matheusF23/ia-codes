import random
import math
from matplotlib import pyplot as plt


def create_population(population_size):
    """Criando população inicial"""
    population = []
    chromosome = []

    while(len(population) != population_size):
        for i in range(64):
            chromosome.append(random.randint(0, 1))

        population.append(chromosome)
        chromosome = []

    return population


def convert_to_float(chromosome):
    decimal = 0
    chromosome = chromosome[::-1]
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            decimal = decimal + 2**i

    float_point = -32.768 + 65.536*(decimal/((2**32) - 1))

    return float_point


def fitness_function(x1, x2):
    return 1/(1+(-20*math.exp(-0.2*math.sqrt((1/2)*(x1**2 + x2**2)))-math.exp((1/2)*(math.cos(2*math.pi*x1)+math.cos(2*math.pi*x2)))+20+math.exp(1)))


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
        for gene in range(len(child)):
            rate = random.random()
            if (rate < mutation_rate):
                child[gene] = 0**child[gene]


def maximizer(population_size, crossing_rate, mutation_rate, generations):
    generation = 0
    population = create_population(population_size)
    mean_list = []  # Guardar os valores médios de aptidão da população
    max_list = []   # Guardar os valores da melhor aptidão da população
    generation_list = []    # Guardar o número de gerações
    while(generation < generations):
        fitness = []
        for chromosome in population:
            x1 = convert_to_float(chromosome[:32])
            x2 = convert_to_float(chromosome[32:])
            fitness.append(fitness_function(x1, x2))

        # Seleciona o melhor cromossomo para passar para a próxima geração
        best_chromosome = population[fitness.index(max(fitness))]

        mean = sum(fitness) / len(fitness)
        generation_list.append(generation)
        mean_list.append(mean)
        max_list.append(max(fitness))

        # É preciso normalizar os valores em fitness entre 0 e 1, para atribuir
        # pesos aos cromossomos na roleta.   .
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
            while True:
                mother = random.choice(roulette)
                if(mother != father):
                    break
            parents.append((father, mother))

        children = crossing_over(parents, crossing_rate)
        mutation(children, mutation_rate)

        # Adicionar o melhor cromossomo no lugar do pior
        fitness_child = []
        for chromosome in children:
            x1 = convert_to_float(chromosome[:32])
            x2 = convert_to_float(chromosome[32:])
            fitness_child.append(fitness_function(x1, x2))
        # if(min(fitness_child) < max(fitness)):
        children[fitness_child.index(min(fitness_child))] = best_chromosome

        population = children[:]
        generation += 1

    best_x1 = convert_to_float(best_chromosome[:32])
    best_x2 = convert_to_float(best_chromosome[32:])
    return (best_x1, best_x2, max(fitness), generation_list, mean_list, max_list)


def plot_result(x, y_mean, y_max):
    plt.figure(num="Aptidão média e melhor aptidão da população")
    plt.plot(x, y_mean, x, y_max, '--')
    plt.title('Aptidão média e melhor aptidão da população')
    plt.legend(('Média', 'Melhor'), loc='best')
    plt.ylabel('Aptidão')
    plt.xlabel('Geração')

    plt.show()


crossing_rate = float(input("Informe a taxa de cruzamento (entre 0 e 1): "))
mutation_rate = float(input("Informe a taxa de mutação (entre 0 e 1): "))
population_size = int(input("Informe o tamanho da população: "))
generations = int(input("Informe a quantidade de gerações: "))

results = maximizer(population_size, crossing_rate, mutation_rate, generations)

print(f'\nMelhor valor de x1: {results[0]}')
print(f'Melhor valor de x2: {results[1]}')
print(f'f(x1,x2): {results[2]}')
plot_result(results[3], results[4], results[5])
