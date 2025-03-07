import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error


file_path = 'data/dataset.csv'
data = pd.read_csv(file_path)

# split the data into features(x) and labels(y)
feature_columns = ["weather", "road_condition", "speed_kmh", "driver_age", "time_of_day"]
target_column = "severity"

X = data[feature_columns]  
y = data[target_column]


# split the data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# test the model
y_pred = model.predict(X_test)

# calculate the metrics after traiining and testing
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"Model Performance:\nMAE: {mae:.2f}\nRMSE: {rmse:.2f}")

# prediction using hypothetical data
sample_input = pd.DataFrame([[1, 1, 80, 30, 2]])  # Rainy, Wet, 80 km/h, Driver age 30, Night
y_sample_pred = model.predict(sample_input)
print(f"Predicted Accident Severity: {y_sample_pred[0]:.2f}")

# save the trained model
joblib.dump(model, "road_accident_model.pkl")
print("Model saved as road_accident_model.pkl")
