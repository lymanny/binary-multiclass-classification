# Sigmoid Function
# Example: Binary Classification

import math


# 1. Sigmoid function
def sigmoid(z):
    return 1 / (1 + math.exp(-z))


# 2. Example value
z = 2

probability = sigmoid(z)

print("z:", z)
print("Sigmoid:", probability)


# 3. Convert probability to class
if probability >= 0.5:
    print("Prediction: Class 1")
else:
    print("Prediction: Class 0")