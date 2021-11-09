import numpy as np


# Sigmoid Activation Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Sigmoid Derivative
def sigmoid_derivative(x):
    return x * (1 - x)


def forward_pass():
    hidden_layer_activation = np.dot(inputs, hidden_weights)
    hidden_layer_activation += hidden_bias
    hidden_layer_output = sigmoid(hidden_layer_activation)
    output_layer_activation = np.dot(hidden_layer_output, output_weights)
    output_layer_activation += output_bias
    predicted_output = sigmoid(output_layer_activation)
    return hidden_layer_output, predicted_output


def backpropagation(output_weights, output_bias, hidden_weights, hidden_bias, lr=0.1):
    error = expected_output - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden_layer = d_predicted_output.dot(output_weights.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)
    # Updating Weights and Biases
    output_weights += hidden_layer_output.T.dot(d_predicted_output) * lr
    output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * lr
    hidden_weights += inputs.T.dot(d_hidden_layer) * lr
    hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * lr


if __name__ == '__main__':
    # Inputs and Expected Outputs
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    expected_output = np.array([[0], [1], [1], [0]])

    # Allocating Weights to neurons
    input_layer_neurons, hidden_layer_neurons, output_layer_neurons = 2, 2, 1
    hidden_weights = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
    hidden_bias = np.random.uniform(size=(1, hidden_layer_neurons))
    output_weights = np.random.uniform(size=(hidden_layer_neurons, output_layer_neurons))
    output_bias = np.random.uniform(size=(1, output_layer_neurons))

    for epochs in range(10000):
        hidden_layer_output, predicted_output = forward_pass()
        backpropagation(output_weights, output_bias, hidden_weights, hidden_bias)

    hidden_layer_output, predicted_output = forward_pass()
    final_predictions = [round(float(prediction)) for prediction in predicted_output]

    print("Finding A XOR B using neural network.")
    print(f'CASE 1: A = 0, B = 0\nA XOR B = {final_predictions[0]}\n')
    print(f'CASE 2: A = 0, B = 1\nA XOR B = {final_predictions[1]}\n')
    print(f'CASE 3: A = 1, B = 0\nA XOR B = {final_predictions[2]}\n')
    print(f'CASE 4: A = 1, B = 1\nA XOR B = {final_predictions[3]}\n')
