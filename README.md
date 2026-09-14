# 🏠 House Price Category Predictor

## Project Overview

This project demonstrates the deployment of a machine learning classification model as an interactive web application using Streamlit.

The application uses a trained **Random Forest Classifier** to predict whether a house belongs to the **Lower Price** or **Higher Price** category based on its characteristics.

The project was developed as part of a Machine Learning Internship and represents the deployment stage of the machine learning project.

---

## Dataset Description

The model was developed using a processed house price dataset containing **2,000 records**.

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

The final model uses **13 input features** after preprocessing.

---

## Machine Learning Model

The final model selected in Task 5 was a:

**Random Forest Classifier**

The baseline Random Forest model was selected as the final model because it achieved the strongest independent test performance among the models evaluated.

### Final Test Performance

| Metric | Score |
|---|---:|
| Accuracy | 56.00% |
| Precision | 55.66% |
| Recall | 59.00% |
| F1 Score | 57.28% |
| ROC-AUC | 54.75% |

Hyperparameter tuning was performed using both **GridSearchCV** and **RandomizedSearchCV**.

The tuned models did not improve the independent test performance of the baseline Random Forest. Therefore, the baseline Random Forest was retained as the final model and deployed in this application.

---

## Application Features

The Streamlit application provides:

- Interactive house information form
- Input validation
- Automatic categorical preprocessing
- Random Forest prediction
- Lower Price / Higher Price classification
- Confidence score
- Prediction probability chart
- Submitted information summary
- Reset functionality
- Prediction history
- Download prediction history as CSV
- Sidebar with project information
- User instructions
- Error handling
- Responsive web interface

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

The 13 model features are:

```text
Area
Bedrooms
Bathrooms
Floors
YearBuilt
Location_Rural
Location_Suburban
Location_Urban
Condition_Fair
Condition_Good
Condition_Poor
Garage_Yes
TotalRooms
```

---

## Model Workflow

The deployed application follows the complete machine learning workflow:

```text
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
```

The trained model is loaded using **Joblib**.

---

## Project Structure

```text
Task6-ML-Deployment/
│
├── app.py
├── final_random_forest_model_task5.joblib
├── requirements.txt
└── README.md
```

### File Description

| File | Description |
|---|---|
| `app.py` | Streamlit web application source code |
| `final_random_forest_model_task5.joblib` | Trained Random Forest model from Task 5 |
| `requirements.txt` | Required Python packages |
| `README.md` | Project documentation |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/maleeha1d2003/Task6-ML-Deployment.git
```

### 2. Open the Project Directory

```bash
cd Task6-ML-Deployment
```

### 3. Install the Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

## Requirements

The application requires the following Python packages:

```text
streamlit
pandas
joblib
scikit-learn==1.7.2
```

These dependencies are listed in `requirements.txt`.

---

## Usage Instructions

1. Open the application.
2. Enter the house area in square feet.
3. Enter the number of bedrooms.
4. Enter the number of bathrooms.
5. Enter the number of floors.
6. Enter the year the house was built.
7. Select the location.
8. Select the house condition.
9. Select whether the house has a garage.
10. Enter the total number of rooms.
11. Click **Predict Price Category**.
12. Review the predicted price category.
13. Review the confidence score.
14. View the prediction probability chart.
15. Review the submitted house information.
16. View prediction history.
17. Download prediction history as a CSV file if required.
18. Use the **Reset** button to restore the default inputs.

---

## Input Validation

The application includes input validation to prevent invalid values.

Examples of validation checks include:

- Area must be greater than zero.
- Bedrooms must be greater than zero.
- Bathrooms must be greater than zero.
- Floors must be greater than zero.
- Year Built cannot be greater than the current year.
- Total Rooms must be greater than or equal to the number of bedrooms.

If invalid input is detected, an appropriate error message is displayed to the user instead of sending invalid data to the model.

---

## Prediction Result

After valid inputs are submitted, the application displays:

- Predicted Price Category
- Predicted Class
- Confidence Score
- Probability for each price category

The two possible prediction classes are:

```text
Lower Price
Higher Price
```

The probability chart provides a visual representation of the model's prediction probabilities.

---

## Optional Enhancements

Two optional enhancements were implemented as part of the deployment.

### 1. Prediction History

The application maintains a prediction history during the current session.

Each prediction records:

- Timestamp
- Area
- Bedrooms
- Bathrooms
- Floors
- Year Built
- Location
- Condition
- Garage
- Total Rooms
- Prediction
- Confidence Score

### 2. Download Predictions as CSV

Users can download their prediction history as a CSV file using the **Download Prediction History as CSV** button.

This allows users to save and review their prediction results for further analysis.

---

## Deployment

The application is deployed using **Streamlit Community Cloud**.

### Live Application

**House Price Category Predictor**

https://house-price-category-predictor.streamlit.app/

The deployed application allows users to enter house characteristics and receive real-time predictions from the trained Random Forest model.

---

## GitHub Repository

The complete source code and trained model are available in the GitHub repository:

https://github.com/maleeha1d2003/Task6-ML-Deployment

The repository contains:

- Streamlit application source code
- Trained Random Forest model
- Requirements file
- Project documentation

---

## Testing

The application was tested locally and after deployment.

Testing confirmed that:

- The Streamlit application launches successfully.
- The trained Random Forest model loads successfully.
- User inputs are accepted correctly.
- Input validation works as expected.
- Categorical variables are automatically converted into the numerical format required by the model.
- Predictions are generated successfully.
- Confidence scores are displayed.
- Prediction probabilities are visualized.
- Submitted information is displayed clearly.
- Multiple predictions can be recorded in prediction history.
- Prediction history can be downloaded as a CSV file.
- The Reset functionality works correctly.
- The deployed application is accessible through the live Streamlit URL.

---

## Screenshots

The project documentation includes screenshots demonstrating:

1. Main application interface and house input form
2. Sidebar and project instructions
3. Prediction result
4. Confidence score
5. Prediction probability chart
6. Submitted house information
7. Prediction history
8. CSV download functionality
9. Input validation
10. Live Streamlit deployment
11. GitHub repository

---

## Technologies Used

- **Python** — Programming language
- **Streamlit** — Web application framework
- **Pandas** — Data manipulation
- **Scikit-learn** — Machine learning
- **Joblib** — Model serialization and loading
- **GitHub** — Source code management
- **Streamlit Community Cloud** — Application deployment

---

## Project Development

The machine learning project was completed through multiple stages, including:

- Data preprocessing
- Exploratory data analysis
- Feature engineering
- Model training
- Model evaluation
- Cross-validation
- Hyperparameter optimization
- Error analysis
- Final model selection
- Model deployment

Task 5 focused on model optimization and final model selection, while Task 6 focused on deploying the selected model as an interactive web application.

---

## Task 6 Objective

The objective of Task 6 was to deploy the final machine learning model as an interactive web application and demonstrate its practical use by allowing users to provide house information and receive real-time predictions.

The deployed application fulfills the required deployment workflow:

```text
User Input
     ↓
Pre-processing
     ↓
Trained Machine Learning Model
     ↓
Prediction
     ↓
Confidence Score
     ↓
Interactive Result
```

---

## Internship Task

**Task 6: Machine Learning Model Deployment**

This project was developed as part of a Machine Learning Internship and demonstrates the practical deployment of a trained machine learning classification model using Streamlit.
