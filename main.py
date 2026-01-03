from truman.nursery import Individual, activate_civilization
from anubia.anubia import DeepLearning
from random import randint, uniform
from truman.utility import make_civilization

num = 1000

X_train = make_civilization(num)

Y_train = []
for x in X_train:
    prob = 0
    if x[0] <= 0.2:
        prob += 0.1
    
    if x[1] >= 0.8:
        prob += 0.1
    
    if x[2] <= 0.4:
        prob += 0.3
    
    if x[3] >= 0.9:
        prob += 0.3
    
    if x[4] >= 0.8:
        prob += 0.2
    
    if x[5] >= 0.7:
        prob += 0.1
    
    Y_train.append([prob])

print(X_train[0], Y_train[0])
truman = DeepLearning(X_train, Y_train, learning_rate=0.01, hidden_layers=[5, 5], activation='tanh')
truman.train(epochs=10e4, verbose=True)