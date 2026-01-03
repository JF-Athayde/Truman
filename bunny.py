from anubia.anubia import DeepLearning
from random import randint, uniform
from truman.utility import make_civilization

num = 10000

X_train = make_civilization(num)

Y_train = [] 
for x in X_train:
    action_tape = [0] * 5

    if 

print(X_train[0], Y_train[0])
truman = DeepLearning(X_train, Y_train, learning_rate=0.01, hidden_layers=[5, 5], activation='tanh')
truman.train(epochs=10e4, verbose=True)
