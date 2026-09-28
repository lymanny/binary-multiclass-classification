# Cross-Entropy Loss
# Example: Multi-class Classification

import math


# Correct class = Orange

# 1. Good prediction
orange_probability = 0.9

loss_good = -math.log(orange_probability)

print("✅ Good Prediction")
print("🍊 Orange Probability:", orange_probability)
print("📉 Cross-Entropy Loss:", loss_good)


# 2. Fairly good prediction
orange_probability = 0.7

loss_medium = -math.log(orange_probability)

print("\n👍 Fairly Good Prediction")
print("🍊 Orange Probability:", orange_probability)
print("📉 Cross-Entropy Loss:", loss_medium)


# 3. Bad prediction
orange_probability = 0.1

loss_bad = -math.log(orange_probability)

print("\n❌ Bad Prediction")
print("🍊 Orange Probability:", orange_probability)
print("📈 Cross-Entropy Loss:", loss_bad)