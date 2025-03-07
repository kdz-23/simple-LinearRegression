import joblib
import pandas as pd

# Load the saved model
model = joblib.load("road_accident_model.pkl")


# Define the feature names
feature_names = ["weather", "road_condition", "speed_kmh", "driver_age", "time_of_day"]


# Prompt the user for input valus
print("Enter the following values to predict accident severity:")
weather = int(input("Weather Condition (0: Clear, 1: Rainy, 2: Snowy): "))
road_condition = int(input("Road Condition (0: Dry, 1: Wet, 2: Icy): "))
speed_kmh = float(input("Vehicle Speed in km/h: "))
driver_age = int(input("Driver Age: "))
time_of_day = int(input("Time of Day (0: Morning, 1: Afternoon, 2: Night): "))

# Create input array

sample_input = pd.DataFrame([[weather, road_condition, speed_kmh, driver_age, time_of_day]], columns=feature_names)

# Make a prediction

predicted_severity = model.predict(sample_input)

# Display the result

print(f"\nPredicted Accident Severity: {predicted_severity[0]:.2f}")
