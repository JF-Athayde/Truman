import random
import numpy as np

def binary(options_receive):
    options = list(options_receive)
    a = max(options)

    result = [0] * len(options)

    result[options.index(a)] = 1

    return result

def print_all_binary(vector):
    for options in vector:
        a = binary(options)
        for b in a:
            print(b, end=' ')
        print()

def print_micronumbers(x):
    if isinstance(x, (float, int, np.floating)):
        print(f'{x:.10f}', end=' ')
    else:
        for v in x:
            print(f'{v:.10f}', end=' ')
    print()

def print_all_micronumbers(x):
    if isinstance(x, (float, int, np.floating)):
        print(f'{x:.10f}')
    else:
        for row in x:
            print_micronumbers(row)

def hit(x):
    if random.uniform(0, 1) < x:
        return True
    return False

def length_branches(k=0.01):
    j = 1
    while True:
        current_probability = 1 - j * k
        if hit(current_probability):
            j += 1
        else:
            break

    return j*k # Galhos, Prob alcançada

def calc_prob(reached_value, k):
    j_final = round(reached_value / k)
    
    prob_sucesso_cumulativa = 1.0
    
    for j in range(1, j_final):
        current_probability_success = 1 - j * k
        prob_sucesso_cumulativa *= current_probability_success
        
        if current_probability_success <= 0:
            return 0.0
        
    prob_falha_final = reached_value
    prob_total = prob_sucesso_cumulativa * prob_falha_final
    
    return prob_total

def note(chromossome):
    s = sum(chromossome.copy()[1:-1])

    current_note = s
    while True:
        if current_note >= 1:
            return round(current_note)
        current_note *= 10

def strength(weight_kg):    
    arm_mass = 0.05 * weight_kg
    force_punch_untrained = arm_mass * 15
    force_punch_trained = arm_mass * 35
    
    return [force_punch_untrained, force_punch_trained]

def make_civilization(num):
    from .nursery import Individual

    civilization = []
    for _ in range(num):
        ind = Individual()
        ind.build()
        # Return primary emotion features: joy, sadness, fear, anger, surprise, disgust
        civilization.append([ind.joy, ind.sadness, ind.fear, ind.anger, ind.surprise, ind.disgust])

    return civilization