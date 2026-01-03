import random
import utility as utility

def crossover_point(size):
    return random.randint(1, size - 1)

def crossover(dna1, dna2, point):
    return dna1[:point] + dna2[point:]

def mutation(dna, mutation_rate=0.05):
    if utility.hit(mutation_rate):
        idx = random.randint(0, len(dna) - 1)
        change = random.choice([-1, 1]) * utility.length_branches()
        dna[idx] = dna[idx] + change
    return dna

def generate_child(dna1, dna2, mutation_rate=0.05):
    size = len(dna1)
    point = crossover_point(size)
    child = crossover(dna1, dna2, point)
    child = mutation(child, mutation_rate)
    return child
