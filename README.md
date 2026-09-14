# 🏠 House Price Category Predictor

## Project Overview

This project demonstrates the deployment of a machine learning classification model as an interactive web application using Streamlit.

The application uses a trained Random Forest Classifier to predict whether a house belongs to the **Lower Price** or **Higher Price** category based on its characteristics.

The project was developed as part of a Machine Learning Internship and represents the deployment stage of the project.

---

## Dataset Description

The model was developed using a processed house price dataset containing 2,000 records.

The original dataset contains information related to:

- Area
- Bedrooms
- Bathrooms
- Floors
- Year Built
- Location
- Condition
- Garage
- Total Rooms
- Price

For the classification task, the continuous `Price` variable was converted into a binary `Price_Category` target using the median price.

The two classes are:

- `0` → Lower Price
- `1` → Higher Price

The model uses 13 input features after preprocessing.

---

## Machine Learning Model

The final model selected in Task 5 was a:

**Random Forest Classifier**

The baseline Random Forest model was selected as the final model because it achieved the strongest independent test performance among the optimized alternatives.

Final test performance:

- Accuracy: 56.00%
- Precision: 55.66%
- Recall: 59.00%
- F1 Score: 57.28%
- ROC-AUC: 54.75%

Hyperparameter tuning was performed using both GridSearchCV and RandomizedSearchCV. The tuned models did not improve the independent test performance of the baseline Random Forest, so the baseline model was retained for deployment.

---

## Application Features

The Streamlit application provides:

- Interactive house information form
- Input validation
- Automatic categorical preprocessing
- Random Forest prediction
- Price category prediction
- Confidence score
- Prediction probability chart
- Submitted information summary
- Reset functionality
- Prediction history
- Download prediction history as CSV
- Sidebar instructions and model information
- Error handling

---

## Input Features

Users provide the following information:

| Feature | Description |
|---|---|
| Area | House area in square feet |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Floors | Number of floors |
| Year Built | Year the house was constructed |
| Location | Rural, Suburban, or Urban |
| Condition | Fair, Good, or Poor |
| Garage | Whether the house has a garage |
| Total Rooms | Total number of rooms |

The categorical inputs are automatically converted into the one-hot encoded format expected by the trained model.

---

## Model Workflow

The application follows this workflow:

User Input  
↓  
Input Validation  
↓  
Data Pre-processing  
↓  
Random Forest Model  
↓  
Prediction  
↓  
Confidence Score  
↓  
Result Display

---

## Project Structure

```text
Task6_ML_Deployment/
│
├── app.py
├── final_random_forest_model_task5.joblib
├── requirements.txt
└── README.md