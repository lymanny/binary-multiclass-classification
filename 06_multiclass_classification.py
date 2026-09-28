# Multi-class Classification
# Example: Study Hours -> Beginner / Intermediate / Advanced

from sklearn.linear_model import LogisticRegression


# 1. Training data
X = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9]
]

# 3 classes
y = [
    "Beginner",
    "Beginner",
    "Beginner",
    "Intermediate",
    "Intermediate",
    "Intermediate",
    "Advanced",
    "Advanced",
    "Advanced"
]


# 2. Create model
model = LogisticRegression(max_iter=1000)


# 3. Train model
model.fit(X, y)


# 4. New student
study_hours = 8


# 5. Predict
prediction = model.predict([[study_hours]])


# 6. Show result
print("📚 Study Hours:", study_hours)
print("🎯 Prediction:", prediction[0])