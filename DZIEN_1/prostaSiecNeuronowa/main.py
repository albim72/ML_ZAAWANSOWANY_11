import numpy as np
from simplenn import SimpleNeuralNetwork

print("Prosta sieć neuronowa ucząca się prostych danych binarnych")

network = SimpleNeuralNetwork()
print(network.weights)

train_inputs = np.array([[1,1,0],[1,1,1],[1,1,0],[1,0,0],[0,1,1],[0,1,0],[0,0,0]])
train_outputs = np.array([[0,1,0,0,1,0,0]]).T

train_iterations = 50000
network.train(train_inputs,train_outputs,train_iterations)

print(network.weights)

print("_________ testowanie sieci _________")
test_data = np.array([[1,1,1],[1,0,0],[0,1,1],[0,1,0],[0,0,0]])

for data in test_data:
    print(f"wynik dla {data} wynosi: {network.propagation(data)}")
