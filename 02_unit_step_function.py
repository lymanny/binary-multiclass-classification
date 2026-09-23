# Unit Step Function
# 0 = Fail
# 1 = Pass


# 1. Unit Step Function
def unit_step(z):
    if z >= 0:
        return 1
    else:
        return 0


# 2. Simple examples
z1 = 2
z2 = -3

print("z =", z1)
print("Output:", unit_step(z1))  # 1 = Pass

print()

print("z =", z2)
print("Output:", unit_step(z2))  # 0 = Fail


# 3. Show Pass / Fail
z = 2
prediction = unit_step(z)

if prediction == 1:
    print("\nPrediction: Pass")
else:
    print("\nPrediction: Fail")


# 4. Limitation: Cannot show confidence
print("\n--- Limitation: No Confidence ---")

print("z = 0.1  ->", unit_step(0.1))
print("z = 10   ->", unit_step(10))

# Both give 1 even though 10 is much stronger than 0.1


# 5. Limitation: Sudden change
print("\n--- Limitation: Sudden Change ---")

print("z = -0.01 ->", unit_step(-0.01))
print("z = 0.01  ->", unit_step(0.01))

# A very small change makes the output jump from 0 to 1