# Binary Classification
# Example: Study Hours -> Pass / Fail

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# 1. Training data
# Each input needs [ ] because scikit-learn expects features
X = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
]

# 0 = Fail
# 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1]


# 2. Create the model
model = LogisticRegression()


# 3. Train the model
model.fit(X, y)


# 4. Check predictions on the data
predictions = model.predict(X)

accuracy = accuracy_score(y, predictions)

print("Accuracy:", accuracy)


# 5. New student
study_hours = 6

new_data = [[study_hours]]


# 6. Predict class
prediction = model.predict(new_data)

# Predict probability
probability = model.predict_proba(new_data)


# 7. Show result
print("\nStudy Hours:", study_hours)

print("Probability of Fail:", probability[0][0])
print("Probability of Pass:", probability[0][1])

if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")