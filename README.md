# Binary & Multi-class Classification

A beginner-friendly Python project for learning the basic concepts of **Binary Classification** and **Multi-class Classification**.

## 📚 Topics

### 🔵 Binary Classification

- Binary Classification
- Unit Step Function
- Sigmoid Function
- BCE (Binary Cross-Entropy) Loss
- MSE Loss vs BCE Loss

### 🟠 Multi-class Classification

- Multi-class Classification
- Softmax Function
- Cross-Entropy Loss


## 🔵 Binary Classification

Binary Classification predicts between **2 possible classes**.

Examples:

```text
Pass / Fail
Disease / No Disease
Spam / Not Spam
```

Basic flow:

```text
Input
  ↓
Model
  ↓
Sigmoid
  ↓
Probability
  ↓
Class 0 or Class 1
```

For Binary Classification:

```text
Sigmoid
   ↓
BCE Loss
```

## 🟠 Multi-class Classification

Multi-class Classification predicts **one class from 3 or more classes**.

Examples:

```text
Cat / Dog / Bird
Apple / Banana / Orange
Beginner / Intermediate / Advanced
```

Basic flow:

```text
Input
  ↓
Model
  ↓
Softmax
  ↓
Probabilities
  ↓
Choose Highest Probability
  ↓
One Class
```

For Multi-class Classification:

```text
Softmax
   ↓
Cross-Entropy Loss
```

## 📉 Loss Functions

```text
Regression
→ MSE Loss

Binary Classification
→ BCE Loss

Multi-class Classification
→ Cross-Entropy Loss
```

Lower loss generally means the model's prediction is closer to the correct answer.

## 📦 Requirements

```text
scikit-learn
```

## 🔗 References

- Python Documentation
- scikit-learn Documentation
- Logistic Regression
- Perceptron
- Binary Classification
- Multi-class Classification
- Sigmoid
- Softmax
- Binary Cross-Entropy Loss
- Cross-Entropy Loss
