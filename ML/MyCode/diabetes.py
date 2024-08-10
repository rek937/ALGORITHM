from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Load the datasets
diabetesSet = datasets.load_diabetes()
diabetes_X = diabetesSet.data
diabetes_y = diabetesSet.target

# Split the dataset into training and testing sets
train_X, test_X, train_y, test_y = train_test_split(diabetes_X, diabetes_y, test_size = 0.2)

# Standardize the datasets
trian_X = StandardScaler().fit_transform(train_X)
test_X = StandardScaler().fit_transform(test_X)

# Add a col of ones to include the bias term
train_X = np.c_[np.ones(train_X.shape[0]), train_X]
test_X = np.c_[np.ones(test_X.shape[0]), test_X]

# # Fit the model
# model = LinearRegression()
# model.fit(train_X, train_y)

# # Predict the values
# predic_train_y = model.predict(train_X)
# predic_test_y = model.predict(test_X)

# # Count the mean square error
# train_err = mean_squared_error(train_y, predic_train_y)
# test_err = mean_squared_error(test_y, predic_test_y)
# print(f"Train mean square error: {train_err:.2f}")
# print(f"Test mean square error: {test_err:.2f}")

# Initialize the parameters
num_iterations = 600
alpha = 0.01
theta = np.zeros(train_X.shape[1])

# Gredient Descent
m = train_X.shape[0]
cost_function_values = []

for i in tqdm(range(num_iterations), desc="Training Progress"):
    predictions = train_X.dot(theta)
    error = predictions - train_y
    gradient = (1 / m) * train_X.T.dot(error)
    theta = theta - alpha * gradient
    cost_value = np.sum((error ** 2)) / (2 * m)
    cost_function_values.append(cost_value)

predictions_train = train_X.dot(theta)
predictions_test = test_X.dot(theta)
print(f"Train mean square error: {mean_squared_error(train_y, predictions_train):.2f}")
print(f"Test mean square error: {mean_squared_error(test_y, predictions_test):.2f}")

plt.plot(range(num_iterations), cost_function_values, label='Cost Function')
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title('Cost Function over Iterations')
plt.legend()
plt.show()
