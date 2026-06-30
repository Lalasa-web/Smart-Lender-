# Smart Lender - Loan Approval Prediction System

## Project Overview

Smart Lender is a Machine Learning-based web application that predicts whether a loan application will be approved or rejected based on applicant details and financial information.

The system uses historical loan application data to train machine learning models and provides real-time loan eligibility predictions through a Flask-based web application.

The main objective of this project is to assist users in understanding loan approval possibilities using data-driven machine learning predictions.

---

# Features

- User-friendly web interface for entering loan details
- Data preprocessing and feature transformation
- Machine Learning based loan approval prediction
- Training and evaluation of multiple classification models
- Automatic selection of the best performing model
- Prediction confidence percentage display
- Flask backend integration
- Saved model deployment using Joblib

---

# Machine Learning Workflow

The project follows the complete Machine Learning lifecycle:

1. Dataset Collection
2. Exploratory Data Analysis
3. Data Cleaning and Preprocessing
4. Feature Encoding
5. Handling Class Imbalance
6. Feature Scaling
7. Model Training
8. Model Evaluation
9. Best Model Selection
10. Flask Application Deployment

---

# Technology Stack

## Programming Language

- Python

## Frontend Technologies

- HTML
- CSS

## Backend Framework

- Flask

## Machine Learning Libraries

- Scikit-learn
- XGBoost
- Pandas
- NumPy
- Joblib

## Development Environment

- Visual Studio Code

## Deployment Platform

- Render

## Version Control

- Git
- GitHub

---

# Machine Learning Models Used

The following classification algorithms were implemented and evaluated:

1. Decision Tree Classifier
2. Random Forest Classifier
3. K-Nearest Neighbor (KNN)
4. XGBoost Classifier

The model with the best performance was selected and saved for deployment.

---

# Dataset Description

The project uses a historical loan prediction dataset.

The dataset contains applicant and financial details used to predict loan approval status.

## Input Features

- Gender
- Marital Status
- Dependents
- Education
- Self Employment Status
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Term
- Credit History
- Property Area

## Target Variable

Loan Status:

- Y → Loan Approved
- N → Loan Rejected

---

# Project Structure

```
Smart-Lender/

│
├── Dataset/
│   └── loan_prediction.csv
│
├── models/
│   ├── best_loan_model.pkl
│   └── preprocessed_loan_data.pkl
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── home.html
│   ├── input.html
│   └── output.html
│
├── app.py
│
├── predict.py
│
├── loan_analysis.ipynb
│
├── loan_modeling.ipynb
│
├── requirements.txt
│
├── README.md
│
└── .gitignore

```

---

# Installation and Setup

## Step 1: Clone Repository

Clone the project from GitHub:

```
git clone https://github.com/Lalasa-web/Smart-Lender-.git
```

Move into the project directory:

```
cd Smart-Lender
```

---

## Step 2: Create Virtual Environment

Create a virtual environment:

```
python -m venv venv
```

Activate the environment:

Windows:

```
venv\Scripts\activate
```

---

## Step 3: Install Dependencies

Install all required libraries:

```
pip install -r requirements.txt
```

---

# Running the Application

Start the Flask application:

```
python app.py
```

The application will run at:

```
http://127.0.0.1:5000/
```

Open this URL in your browser.

---

# Application Workflow

The prediction process works as follows:

User enters loan application details

↓

Flask receives the input data

↓

Categorical values are encoded using saved label encoders

↓

Numerical features are scaled using StandardScaler

↓

The trained Machine Learning model predicts loan status

↓

The application displays:

- Loan Approved
- Loan Rejected

with prediction confidence percentage.

---

# Model Saving and Loading

The trained model and preprocessing objects are saved using Joblib.

## best_loan_model.pkl

Contains:

- Best performing trained Machine Learning model
- StandardScaler used during preprocessing

## preprocessed_loan_data.pkl

Contains:

- Label encoders
- Preprocessing information

These files are loaded by the Flask application during prediction.

---

# Application Pages

## Home Page

Provides project introduction and navigation.

## Input Page

Allows users to enter loan application details.

## Output Page

Displays:

- Loan prediction result
- Confidence score

---

# Testing

The application was tested for:

- Model prediction functionality
- User input handling
- Flask routing
- Application response time

Performance testing was performed using Apache JMeter.

---

# Deployment

The Smart Lender application is deployed using Render Cloud Platform.

Deployment URL:

https://smart-lender-i9fg.onrender.com

---

# Limitations

- Predictions depend on historical dataset patterns.
- No real-time banking data integration.
- No authentication system is implemented.
- Prediction is performed for one applicant at a time.
- Model accuracy depends on dataset quality.

---

# Future Enhancements

Future improvements include:

- User authentication and authorization
- Integration with banking APIs
- Loan analytics dashboard
- Improved model tuning
- Larger and updated datasets
- Mobile application support
- Advanced reporting features

---

# Author

Lalasa Annam
