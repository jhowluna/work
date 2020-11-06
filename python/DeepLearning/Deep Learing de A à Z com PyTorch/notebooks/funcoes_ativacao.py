import numpy as np

def stepFunction(soma):
    if(soma >= 1):
       return 1
    return 0

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def hyperbolicTangent(soma):
    return (np.exp(soma) - np.exp(- soma)) / (np.exp(soma) + np.exp(- soma))

def relu(soma):
    if soma >= 0:
        return soma
    return 0
def linear(soma):
    return soma

def softmax(x):
    ex = np.exp(x)
    return ex / ex.sum()

soma = -0.358

teste = stepFunction(soma)
print(teste)

teste = sigmoid(soma)
print(teste)

teste = hyperbolicTangent(soma)
print(teste)

teste = relu(soma)
print(teste)

valores = [10.0,2.0,1.3]

teste = softmax(valores)
print(teste)
