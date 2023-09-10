import numpy as np

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Input data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Target labels
y = np.array([
    [0],    
    [1],
    [1],
    [0]
])

# Seed the random number generator for reproducibility
np.random.seed(42)

# Initialize the weights randomly with mean 0
input_neurons = 2
hidden_neurons = 4
output_neurons = 1

# Initialize weights for the first and second layers
weights_input_hidden = 2 * np.random.random((input_neurons, hidden_neurons)) - 1
weights_hidden_output = 2 * np.random.random((hidden_neurons, output_neurons)) - 1

# Learning rate
learning_rate = 0.1

# Training
for iteration in range(10000):
    # Forward propagation
    hidden_layer_input = np.dot(X, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    output_layer_output = sigmoid(output_layer_input)
    
    # Calculate the error
    error = y - output_layer_output
    
    # Backpropagation
    d_output = error * sigmoid_derivative(output_layer_output)
    
    error_hidden_layer = d_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)
    
    # Update weights
    weights_hidden_output += hidden_layer_output.T.dot(d_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate

# Test the neural network
test_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
test_output = sigmoid(np.dot(sigmoid(np.dot(test_input, weights_input_hidden)), weights_hidden_output))

print("Predicted Output:")
print(test_output)
