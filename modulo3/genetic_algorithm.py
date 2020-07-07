"""
Objetivo: maximizar a função f(x)
f(x) = 15x - x^2
x: 0 ... 15
"""

import random


# def convert_to_decimal(chromosome):
#     signal = chromosome[0]   # bit de sinal
#     decimal = 0
#     chromosome = chromosome[:0:-1]
#     length = len(chromosome)
#     for i in range(length):
#         if chromosome[i] == 1:
#             decimal = decimal + 2**i
#     if(signal == '0'):  # Número positivo
#         return decimal
#     else:
#         return decimal * (-1)   # Retorna um inteiro
#     return decimal


def convert_to_decimal(chromosome):
    decimal = 0
    chromosome = chromosome[::-1]
    length = len(chromosome)
    for i in range(length):
        if chromosome[i] == 1:
            decimal = decimal + 2**i

    return decimal


def convert_to_chromosome(decimal):
    chromosome = []
    while(True):
        chromosome.append(decimal%2)
        decimal = decimal//2
        if decimal == 0:
            break
    
    while(len(chromosome) < 4 ):
        chromosome.append(0)

    chromosome = chromosome[::-1]
    return chromosome


def resolve_function(x):
    return 15*x - x**2


def create_population(population_size):
    population = []
    chromosome = []

    # Criando população inicial
    while(len(population) != population_size):
        for i in range(4):
            chromosome.append(random.randint(0, 1))

        if(chromosome not in population):
            population.append(chromosome)

        chromosome = []

    return population


# crossing_rate = float(input("Informe a taxa de cruzamento (entre 0 e 1): "))
# mutation_rate = float(input("Informe a taxa de mutação (entre 0 e 1): "))
population_size = int(input("Informe o tamanho da população: "))
# generations = int(input("Informe a quantidade de gerações: "))

for i in create_population(population_size):
    print(i)
    x = convert_to_decimal(i)
    print(x)
    print(convert_to_chromosome(x), '\n')
