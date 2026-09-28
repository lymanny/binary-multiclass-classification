# MSE Loss vs BCE Loss
# Simple examples of their weaknesses

import math


# -------------------------
# 1. MSE Loss
# -------------------------

def mse_loss(real, prediction):
    return (real - prediction) ** 2


print("📊 MSE Loss")

# Small error
real = 100
prediction = 90

mse1 = mse_loss(real, prediction)

print("Real:", real)
print("Prediction:", prediction)
print("MSE Loss:", mse1)


# Large error
real = 100
prediction = 0

mse2 = mse_loss(real, prediction)

print("\n⚠️ Large Error")
print("Real:", real)
print("Prediction:", prediction)
print("MSE Loss:", mse2)


# -------------------------
# 2. BCE Loss
# -------------------------

def bce_loss(y, p):
    return -(y * math.log(p) + (1 - y) * math.log(1 - p))


print("\n📊 BCE Loss")

# Real answer = 1
y = 1


# Good prediction
p_good = 0.9
loss_good = bce_loss(y, p_good)

print("\n✅ Good Prediction")
print("Real Answer:", y)
print("Prediction:", p_good)
print("BCE Loss:", loss_good)


# Wrong prediction
p_bad = 0.1
loss_bad = bce_loss(y, p_bad)

print("\n❌ Wrong Prediction")
print("Real Answer:", y)
print("Prediction:", p_bad)
print("BCE Loss:", loss_bad)


# Very confident wrong prediction
p_very_bad = 0.001
loss_very_bad = bce_loss(y, p_very_bad)

print("\n🚨 Very Confident Wrong Prediction")
print("Real Answer:", y)
print("Prediction:", p_very_bad)
print("BCE Loss:", loss_very_bad)