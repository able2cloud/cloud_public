from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import make_regression
import joblib

# Generate some sample data
X, y = make_regression(n_samples=100, n_features=1, noise=0.1)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Calculate the mean squared error of the model
mse = mean_squared_error(y_test, model.predict(X_test))
print(f"Mean Squared Error: {mse}")

# Save the model to a file
joblib.dump(model, 'model.pkl')

