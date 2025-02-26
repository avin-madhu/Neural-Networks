def calculate_net_input(inputs,weights,bias):
    Y_in = 0
    for i in range(len(inputs)):
        Y_in += inputs[i] * weights[i]
    Y_in += bias
    return Y_in

# basically a step function
def activation_function(net_input):
    if net_input > 0:
        return 1
    elif net_input == 0:
        return 0
    else:
        return -1

# calculate the weight change
def calculate_weight_change(inputs,target, alpha):
    weight_change = []
    for i in range(len(inputs)):
        weight_change.append(alpha * target * inputs[i])
    weight_change.append(alpha * target)
    return weight_change

# updating weights (basically adding the two lists)
def update_weights(weights, weight_change):
    new_weights = []
    for i in range(len(weights)):
        new_weights.append(weights[i] + weight_change[i])
    print(new_weights, "updated weights")
    return new_weights