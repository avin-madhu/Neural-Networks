from utility_functions import *

class perceptron():
    inputs, weights, bias, output, targets, net_input, alpha = None, None, None, None, None, None, None
    def __init__(self):
        self.inputs = [
            [1,1,1,1],
            [-1,1,-1,-1],
            [1,1,1,-1],
            [1,-1,-1,1]
        ]
        self.bias = 0
        self.weights = [0,0,0,0,self.bias]
        self.targets = [1,1,-1,-1]
        self.alpha = 1

        self.net_input = []
        self.epoch = 0

    def training(self):
        while(True):
            initial_weights = self.weights
            self.epoch += 1
            print('EPOCH '+ str(self.epoch))
            for i in range(len(self.inputs)):
                self.net_input = calculate_net_input(self.inputs[i], self.weights, self.bias)
                self.output = activation_function(self.net_input)
                self.weight_change = calculate_weight_change(self.inputs[i], self.targets[i], self.alpha)
                if(self.targets[i] != self.output):
                    self.weights = update_weights(self.weights, self.weight_change)
                self.bias = self.weights[-1]

                print("input: ", self.inputs[i])
                print("Target: ",self.targets[i])
                print("Net Input ", self.net_input)
                print("output: ", self.output)
                print("Weight Change: ",self.weight_change)
                print("Weights: ", self.weights)
                print("\n\n\n")

            if(initial_weights == self.weights):
                break

def main():
    obj  = perceptron()
    obj.training()

if __name__ == "__main__":
    main()
        




