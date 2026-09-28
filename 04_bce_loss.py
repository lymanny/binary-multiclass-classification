# BCE (Binary Cross-Entropy) Loss
# Lower loss = better prediction

import math


# BCE function
def bce_loss(y, p):
    return -(y * math.log(p) + (1 - y) * math.log(1 - p))


# Real answer
y = 1


# Good prediction
p_good = 0.9
loss_good = bce_loss(y, p_good)

print("✅ Good Prediction")
print("🎯 Real Answer:", y)
print("📊 Prediction:", p_good)
print("📉 BCE Loss:", loss_good)


# Bad prediction
p_bad = 0.1
loss_bad = bce_loss(y, p_bad)

print("\n❌ Bad Prediction")
print("🎯 Real Answer:", y)
print("📊 Prediction:", p_bad)
print("📈 BCE Loss:", loss_bad)