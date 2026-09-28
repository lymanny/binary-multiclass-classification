# Softmax Function
# Example: Apple / Banana / Orange

import math


# 1. Model raw scores
scores = [1, 2, 4]

print("Raw Scores:", scores)


# 2. SOFTMAX IS USED HERE
# Softmax changes raw scores into probabilities

exp_scores = [math.exp(score) for score in scores]

total = sum(exp_scores)

probabilities = [
    score / total
    for score in exp_scores
]


# 3. Classes
classes = ["Apple", "Banana", "Orange"]


# 4. Show probabilities
print("\n📊 Softmax Probabilities:")

for class_name, probability in zip(classes, probabilities):
    print(
        class_name,
        ":",
        round(probability * 100, 2),
        "%"
    )


# 5. Choose highest probability
highest_index = probabilities.index(max(probabilities))

prediction = classes[highest_index]


print("\n🎯 Prediction:", prediction)