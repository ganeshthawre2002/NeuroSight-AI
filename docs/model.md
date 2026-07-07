# NeuroSight AI Machine Learning Documentation

## Overview

NeuroSight AI uses a supervised machine learning model to predict whether a customer is likely to churn. The model analyzes customer demographics, account information, subscribed services, and billing behavior to estimate churn probability.

---

# Problem Statement

Customer churn is one of the most important business challenges for subscription-based companies. Predicting churn allows organizations to proactively retain customers and reduce revenue loss.

This project frames churn prediction as a **binary classification** problem.

Target Variable:

* **Yes** → Customer will churn
* **No** → Customer will remain

---

# Dataset

Dataset: Telco Customer Churn

Approximate records:

* 7,043 customers

Target column:

* Churn

Feature categories include:

### Customer Information

* Gender
* Senior Citizen
* Partner
* Dependents

### Account Information

* Tenure
* Contract
* Paperless Billing
* Payment Method

### Services

* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies

### Financial Information

* Monthly Charges
* Total Charges

---

# Data Preprocessing

The preprocessing pipeline performs:

* Missing value handling
* Data type conversion
* Numerical feature scaling
* Categorical feature encoding
* Feature transformation using Scikit-learn pipelines

This ensures that training and inference use identical preprocessing steps.

---

# Model

Algorithm:

* Logistic Regression

Library:

* Scikit-learn

Reasons for choosing Logistic Regression:

* Fast to train
* Interpretable
* Strong baseline for binary classification
* Produces probability scores
* Easy to deploy in production

---

# Training Pipeline

Training workflow:

1. Load dataset
2. Clean data
3. Separate features and target
4. Split into training and testing sets
5. Build preprocessing pipeline
6. Train Logistic Regression model
7. Evaluate model
8. Save trained model using Joblib

---

# Evaluation Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Confusion Matrix
* Classification Report

These metrics provide a balanced assessment of model performance.

---

# Prediction Workflow

When a prediction request is received:

1. User submits customer information.
2. FastAPI validates the request using Pydantic.
3. Prediction service loads the trained model.
4. Preprocessing pipeline transforms the input.
5. The model generates:

   * Churn prediction
   * Churn probability
6. Results are returned to the API and displayed in the Streamlit dashboard.

---

# Model Limitations

Current limitations include:

* Uses a single Logistic Regression model
* Trained on one dataset
* No hyperparameter optimization
* No feature importance visualization
* No explainability techniques such as SHAP or LIME
* No automatic retraining pipeline

---

# Future Improvements

Planned enhancements:

* Random Forest
* XGBoost
* LightGBM
* CatBoost
* Hyperparameter tuning
* Cross-validation
* Feature importance analysis
* SHAP explainability
* Automated retraining
* Model versioning
* MLflow experiment tracking
* Drift detection and monitoring

---

# Business Value

The model enables organizations to:

* Identify customers at high risk of churn
* Prioritize retention campaigns
* Reduce revenue loss
* Support data-driven decision making
* Improve customer lifetime value (CLV)

---

# Conclusion

The machine learning component transforms NeuroSight AI from a traditional analytics dashboard into an intelligent decision-support platform. By combining predictive modeling with business analytics and interactive visualizations, the system helps organizations anticipate customer churn and take proactive retention actions.
