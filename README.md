# 🎓 Student Performance Prediction

An end-to-end Machine Learning application that predicts a student's final academic performance based on demographic, socioeconomic, academic, and lifestyle-related attributes.

The project covers the complete Machine Learning workflow — from data preprocessing and exploratory data analysis to model training, evaluation, and deployment using Flask and Render.

---

## 🚀 Live Demo

🌐 **Live Application:**  
https://student-performance-prediction-jejd.onrender.com

---

## ✨ Features

- 📊 Exploratory Data Analysis
- 🧹 Data preprocessing and feature preparation
- 🔤 Categorical feature encoding using One-Hot Encoding
- 🌲 Random Forest Regression
- ⚙️ Hyperparameter tuning using GridSearchCV
- 📈 Model evaluation using MAE, RMSE, and R²
- 💾 Trained model saved using Joblib
- 🌐 Flask-based web application
- 🚀 Deployed on Render
- 🎯 Real-time student performance prediction

---

## 🔄 Machine Learning Workflow

```text
Student Dataset
      │
      ▼
Data Loading
      │
      ▼
Data Inspection & Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Selection
      │
      ▼
Train-Test Split
      │
      ▼
Data Preprocessing
 ┌────┴──────────────┐
 │                   │
Categorical       Numerical
Features           Features
 │                   │
 ▼                   ▼
One-Hot Encoding   Passthrough
 └───────┬───────────┘
         ▼
Random Forest Model
         │
         ▼
Hyperparameter Tuning
         │
         ▼
Model Evaluation
         │
         ▼
Final Model Training
         │
         ▼
student_performance_model.pkl
         │
         ▼
Flask Web Application
         │
         ▼
Render Deployment
         │
         ▼
Student Performance Prediction
```

---

## 📊 Model Performance

The final model uses a tuned **Random Forest Regressor** to predict the student's final grade (`G3`) on a scale of 0–20.

| Metric | Score |
|---|---:|
| MAE | 2.992 |
| RMSE | 3.756 |
| R² Score | 0.312 |

### Model Configuration

- **Algorithm:** Random Forest Regressor
- **Number of Trees:** 300
- **Maximum Depth:** 15
- **Minimum Samples Split:** 5
- **Minimum Samples Leaf:** 1
- **Hyperparameter Tuning:** GridSearchCV

> **Note:** `G1` and `G2` were excluded from the input features so that the model predicts final performance without directly relying on the student's earlier period grades.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computation |
| Matplotlib | Data visualization |
| Seaborn | Exploratory data visualization |
| Scikit-learn | Machine learning, preprocessing, and evaluation |
| Joblib | Model serialization |
| Flask | Web application backend |
| HTML | Web interface |
| CSS | Web interface styling |
| Jupyter Notebook | ML experimentation and analysis |
| Git & GitHub | Version control and project hosting |
| Render | Application deployment |

---

## 📁 Project Structure

```text
student-performance-prediction/
│
├── dataset/
│   └── student-mat.csv
│
├── model/
│   └── student_performance_model.pkl
│
├── notebooks/
│   └── student_performance.ipynb
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── requirements.txt
├── .python-version
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sakshianupriya29/student-performance-prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd student-performance-prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```powershell
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application Locally

Start the Flask application:

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

Open the URL in your browser and enter the student's information to generate a predicted final grade.

---

## 🧪 Testing

The project was tested at multiple stages of development.

### Model Testing

The final Random Forest model was evaluated using an untouched test set.

| Metric | Result |
|---|---:|
| MAE | 2.992 |
| RMSE | 3.756 |
| R² | 0.312 |

### Application Testing

The Flask application was tested locally to verify:

- Student input submission
- Form data processing
- Model loading
- Prediction generation
- Prediction display

### Deployment Testing

The deployed application was tested on Render using the live web interface.

The application successfully generated predictions from submitted student information.

Example:

```text
Predicted Final Grade: 11.64 / 20
```

---

## 🌐 Deployment

The Flask application is deployed using **Render**.

The production server uses Gunicorn:

```bash
gunicorn app:app
```

Python 3.12 is specified using the `.python-version` file.

The application is deployed from the `main` branch of the GitHub repository.

### Live Application

🌐 https://student-performance-prediction-jejd.onrender.com

> **Note:** The application is hosted on Render's free instance. The service may spin down after a period of inactivity, which can make the first request after inactivity take longer.

---

## 📚 Dataset

The project uses the **UCI Student Performance Dataset**, specifically the Mathematics dataset (`student-mat.csv`).

The dataset contains demographic, family, academic, social, and lifestyle-related attributes of students.

### Prediction Target

```text
G3 — Final Grade
```

The final grade is represented on a scale from **0 to 20**.

The first-period (`G1`) and second-period (`G2`) grades were excluded from the model inputs.

---

## 🔍 Key Machine Learning Steps

### Data Preprocessing

- Loaded the dataset using Pandas
- Inspected dataset structure and data types
- Checked for missing values
- Checked for duplicate records
- Identified numerical and categorical features
- Applied One-Hot Encoding to categorical variables

### Exploratory Data Analysis

The project explored relationships between student attributes and final performance using:

- Grade distribution analysis
- Study time vs. final grade
- Absences vs. final grade
- Descriptive statistics
- Data visualizations using Matplotlib and Seaborn

### Model Development

Multiple regression algorithms were evaluated:

- Linear Regression
- Random Forest Regression
- Gradient Boosting Regression
- Decision Tree Regression
- K-Nearest Neighbors
- Support Vector Regression

The final model uses a tuned Random Forest Regressor.

---

## ⚠️ Limitations

- The model is trained on a relatively small dataset.
- Predictions are estimates and should not be treated as official academic assessments.
- Student performance can be influenced by factors that are not represented in the dataset.
- Model performance may vary when applied to students from different educational systems or populations.
- The current application focuses on predicting the final Mathematics grade.

---

## 🔮 Future Improvements

- Add additional regression and ensemble models
- Improve model performance through feature engineering
- Add model explainability using SHAP
- Add interactive data visualizations
- Add prediction confidence or uncertainty estimates
- Support additional subjects and datasets
- Improve the web application's UI/UX
- Add user authentication and prediction history
- Deploy using scalable production infrastructure

---

## 👩‍💻 Author

**Anupriya Sakshi**

B.Tech Student | Data Analytics & Machine Learning

GitHub: [sakshianupriya29](https://github.com/sakshianupriya29)

---

## ⭐ Acknowledgements

- UCI Machine Learning Repository for the Student Performance Dataset
- Scikit-learn for machine learning tools
- Flask for web application development
- Render for application deployment