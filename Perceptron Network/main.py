from utility_functions import *

inputs = [
    [1,1,1,1],
    [-1,1,-1,-1],
    [1,1,1,-1],
    [1,-1,-1,1]
]
bias = 0
weights = [0,0,0,0,bias]
targets = [1,1,-1,-1]
alpha = 1

net_input = []
epoch = 0

while(True):
    initial_weights = weights
    epoch += 1
    print('EPOCH '+ str(epoch))
    for i in range(len(inputs)):
        net_input = calculate_net_input(inputs[i], weights, bias)
        output = activation_function(net_input)
        weight_change = calculate_weight_change(inputs[i], targets[i], alpha)
        if(targets[i] != output):
            weights = update_weights(weights,weight_change)
        bias = weights[-1]

        print("input: ", inputs[i])
        print("Target: ",targets[i])
        print("Net Input ", net_input)
        print("output: ", output)
        print("Weight Change: ",weight_change)
        print("Weights: ",weights)
        print("\n\n\n")

    if(initial_weights == weights):
        break
        




