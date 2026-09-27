import os
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


# ==========================================
# 1. Load Dataset
# ==========================================

dataset_path = "dataset/student-mat.csv"

df = pd.read_csv(dataset_path, sep=";")

print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)


# ==========================================
# 2. Define Features and Target
# ==========================================

# G3 is the final grade and therefore the target.
#
# G1 and G2 are previous-period grades.
# They are excluded so that the model predicts
# performance without directly using previous grades.

X = df.drop(columns=["G3", "G1", "G2"])
y = df["G3"]


# ==========================================
# 3. Identify Feature Types
# ==========================================

categorical_features = X.select_dtypes(
    include=["object", "string"]
).columns.tolist()

numerical_features = X.select_dtypes(
    exclude=["object", "string"]
).columns.tolist()


# ==========================================
# 4. Preprocessing
# ==========================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "numerical",
            "passthrough",
            numerical_features
        )
    ]
)


# ==========================================
# 5. Train-Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ==========================================
# 6. Create Random Forest Pipeline
# ==========================================

model = Pipeline([
    (
        "preprocessor",
        preprocessor
    ),
    (
        "model",
        RandomForestRegressor(
            n_estimators=300,
            max_depth=15,
            min_samples_split=5,
            min_samples_leaf=1,
            random_state=42
        )
    )
])


# ==========================================
# 7. Train for Evaluation
# ==========================================

model.fit(X_train, y_train)

y_pred = model.predict(X_test)


# ==========================================
# 8. Evaluate Model
# ==========================================

mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(
    y_test,
    y_pred
) ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("----------------------------")
print("MAE :", round(mae, 3))
print("RMSE:", round(rmse, 3))
print("R²  :", round(r2, 3))


# ==========================================
# 9. Train Final Model on Full Dataset
# ==========================================

print("\nTraining final model on complete dataset...")

final_model = Pipeline([
    (
        "preprocessor",
        preprocessor
    ),
    (
        "model",
        RandomForestRegressor(
            n_estimators=300,
            max_depth=15,
            min_samples_split=5,
            min_samples_leaf=1,
            random_state=42
        )
    )
])

final_model.fit(X, y)


# ==========================================
# 10. Save Model
# ==========================================

os.makedirs("model", exist_ok=True)

model_path = "model/student_performance_model.pkl"

joblib.dump(final_model, model_path)

print("\nFinal model saved successfully!")
print("Location:", model_path)