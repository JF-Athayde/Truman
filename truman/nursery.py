from .utility import length_branches, strength
import random

def activate_civilization(civilization):
    for ind in civilization:
        ind.build() # Welcome ind.name

class Individual:
    def __init__(self):
        self.life = 100 # Life Score
        self.name = ''
        
        self.joy = None
        self.sadness = None
        self.fear = None
        self.anger = None
        self.surprise = None
        self.disgust = None

        self.biological_needs = 0

        self.height = None
        self.imc = None
        self.weight = None
        self.strength = None

        self.chromosome = [self.life, self.joy, self.sadness, self.fear, self.anger, self.surprise, self.disgust, self.biological_needs, self.height, self.imc, self.weight, self.strength]  # Person Genetic Ribbon

        self.position = (None, None)
        self.relationships = []

    def build(self):
        self.joy = length_branches(0.001)
        self.sadness = length_branches(0.001)
        self.fear = length_branches(0.001)
        self.anger = length_branches(0.001)
        self.surprise = length_branches(0.001) 
        self.disgust = length_branches(0.001) 

        self.height = (length_branches(0.02) + 1.50) / 1.5 + 1
        self.imc = (random.uniform(17, 41.5)) / 41.5
        self.weight = (random.uniform(self.imc * (self.height ** 2), self.imc * (self.height ** 2))) / (41.5 * 2.5 ** 2)
        self.strength = random.choice(strength(self.weight))

        self.chromosome = [self.life, self.joy, self.sadness, self.fear, self.anger, self.surprise, self.disgust, self.biological_needs, self.height, self.imc, self.weight, self.strength]  # Person Genetic Ribbon

        vowels = list('aeiou')
        consonants = list('bcdfghjklmnpqrstvwxyz')

        for _ in range(0, 3):
            self.name += random.choice(consonants) + random.choice(vowels)
