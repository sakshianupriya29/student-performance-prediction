# Student Performance Prediction

A machine learning web application that predicts a student's final academic
performance based on demographic, socioeconomic, academic-support,
behavioral, and attendance-related attributes.

The project uses a Random Forest Regression model and integrates the trained
model with a Flask web application.

---

## Project Overview

Student performance can be influenced by several factors such as study time,
past failures, family background, educational support, social activities,
health, and attendance.

This project uses the UCI Student Performance dataset to build a machine
learning model that predicts the final student grade (G3).

The model intentionally excludes G1 and G2, which represent previous-period
grades, so that the prediction is based on other student characteristics
rather than directly relying on previous grades.

---

## Features

The model uses 30 input features, including:

### Demographic Features
- School
- Gender
- Age
- Address
- Family size
- Parent status

### Family & Socioeconomic Features
- Mother's education
- Father's education
- Mother's job
- Father's job
- Guardian
- Family educational support

### Academic Features
- Travel time
- Study time
- Past failures
- Extra educational support
- Paid classes
- Higher education intention

### Social & Lifestyle Features
- Extra activities
- Nursery education
- Internet access
- Romantic relationship
- Family relationship quality
- Free time
- Going out
- Workday alcohol consumption
- Weekend alcohol consumption
- Health status
- Number of absences

---

## Target Variable

The target variable is:

**G3 — Final Grade**

The final grade is represented on a scale from 0 to 20.

---

## Dataset

The project uses the UCI Student Performance dataset.

The dataset contains information about students and their academic,
demographic, social, and family-related characteristics.

The mathematics dataset contains:

- 395 student records
- 33 original columns

After removing G1, G2, and G3 from the input data, the model uses
30 predictive features.

---

## Machine Learning Workflow

The project follows the following workflow:

1. Dataset collection
2. Data loading
3. Data inspection
4. Missing-value and duplicate checks
5. Exploratory Data Analysis
6. Feature and target separation
7. Removal of G1 and G2
8. Categorical feature encoding
9. Train-test splitting
10. Model training
11. Model comparison
12. Hyperparameter tuning
13. Model evaluation
14. Final model training
15. Model serialization using Joblib
16. Flask web application integration

---

## Exploratory Data Analysis

Several visualizations were created during the analysis, including:

- Distribution of final grades
- Study time vs final grade
- Absences vs final grade
- Actual vs predicted final grades

These visualizations were used to understand the dataset and evaluate model
behavior.

---

## Models Tested

The following regression algorithms were evaluated:

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 3.395 | 4.196 | 0.141 |
| Random Forest | 3.040 | 3.806 | 0.294 |
| Gradient Boosting | 3.277 | 4.009 | 0.216 |
| Decision Tree | 3.508 | 4.592 | -0.028 |
| KNN | 3.261 | 4.069 | 0.193 |
| SVR | 3.353 | 4.092 | 0.183 |

Random Forest was selected for further tuning based on the evaluation results.

---

## Hyperparameter Tuning

The Random Forest model was tuned using cross-validation.

Final hyperparameters:

```text
n_estimators = 300
max_depth = 15
min_samples_split = 5
min_samples_leaf = 1
random_state = 42