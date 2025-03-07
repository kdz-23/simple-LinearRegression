# A Simple Linear Regression for Road Accident Severity Prediction

This project uses a linear regression model to predict road accident severity based on factors such as vehicle speed and driver age. The model is trained using a dataset (`project_data.csv`) and can be used to make predictions via a user-friendly script (`predictor.py`).

## Repository Contents
- `model.py`: Script to train the linear regression model and save it as `simple_road_accident_severity_model.pkl`.
- `predictor.py`: Script to prompt the user for input values and predict accident severity using the trained model.
- `data/`: Folder containing the dataset (`data.csv`) used to train the model.
- `road_accident_severity_model.pkl`: The trained model file.
- Screenshots: Images showing model performance or results.

## Setup Instructions

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/username/road-accident-severity-model.git
   cd road-accident-severity-model
   
2. **Create a virtual environment and activate it**
   ```bash
   python3 -m venv <environment_name>

   source <environment_name>/bin/activate
3. **Install the necessary dependencies into the created environment**
   ```bash
   pip3 install scikit-learn pandas joblib

4. **Train the model**
   - use the command below to train the created model by running the main model script. this creates and saves as (road_accident_model.pkl)the model for future use
   ```bash
   python3 model.py

5. **The predictor**
 The predictor.py script loads the trained model and allows users to predict accident severity by entering values interactively.
- ensure the virtual environment is active and run the script as below, the user is prompted for the values and the model will predict the severity
  ```bash
  python3 predictor.py
- Prompts the gets are as followed
```bash
Enter the following values to predict accident severity:
Weather Condition (0: Clear, 1: Rainy, 2: Snowy): [Enter 0, 1, or 2]
Road Condition (0: Dry, 1: Wet, 2: Icy): [Enter 0, 1, or 2]
Vehicle Speed in km/h: [Enter a number, e.g., 80]
Driver Age: [Enter a number, e.g., 35]
Time of Day (0: Morning, 1: Afternoon, 2: Night): [Enter 0, 1, or 2]   
  
