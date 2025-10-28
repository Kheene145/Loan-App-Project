# Loan Approval App

## Project Overview

This project is a machine learning web application that predicts whether a loan application will be approved or rejected based on applicant data such as income, credit history, employment status, and other relevant features.

It was developed first in Jupyter Notebook for exploratory data analysis (EDA) and model training, and later deployed using PyCharm and Streamlit for a user-friendly interface.

---
### Objectives

Build a predictive model for loan approval classification.

Perform data preprocessing, feature scaling, and model evaluation.

Save trained models using pickle for reuse.

Create a simple and interactive web app using Streamlit.

### Tools & Libraries Used
Programming Language	Python
IDE / Environment	Jupyter Notebook → PyCharm
Data Analysis & ML	pandas, numpy, scikit-learn
Model Saving	pickle
Web Framework	Streamlit
Version Control	Git & GitHub

loan_approval_project/
│
├── loan_approval_dataset.csv       # Dataset used for model training
├── loan_approval_pred.ipynb        # Jupyter Notebook (EDA + Model Training)
├── loan_app.py                     # Streamlit web app
├── model.pk1                       # Saved trained ML model
├── scaler.pk1                      # Saved data scaler
├── README.md                       # Project documentation
└── .idea/                          # PyCharm configuration files

📊 Model Development Steps

Data Loading & Cleaning – Removed nulls and encoded categorical features.

Feature Scaling – Standardized features using StandardScaler.

Model Training – Trained classification models (e.g., Logistic Regression).

Model Evaluation – Used metrics such as accuracy, confusion matrix, and R².

Model Saving – Saved the trained model and scaler using pickle.

Workflow

Model trained and saved in Jupyter Notebook.

Streamlit app created in PyCharm.

Git initialized locally with git init.

Project pushed to GitHub repository.

🚀 Future Improvements

Add multiple model options (e.g., Random Forest, XGBoost).

Integrate database for storing user input and predictions.

Enhance Streamlit UI with better visuals and explanations.
