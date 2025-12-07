import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# ---------------------------------------------------------
# 1. Load the dataset
# ---------------------------------------------------------
df = pd.read_csv("oil_filter_dataset_2000.csv")

# Drop date columns because model will use calculated feature (age days)
df = df.drop(columns=["oil_filter_change_date", "current_date"])

# ---------------------------------------------------------
# 2. Split input features and target
# ---------------------------------------------------------
X = df.drop("oil_filter_condition", axis=1)
y = df["oil_filter_condition"]

# ---------------------------------------------------------
# 3. Train-test split (1600 train, 400 test)
# ---------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=1600, test_size=400, shuffle=True, random_state=42
)

print("Training rows :", X_train.shape[0])
print("Testing rows  :", X_test.shape[0])

# ---------------------------------------------------------
# 4. Preprocessing setup
# ---------------------------------------------------------
num_cols = [
    "engine_capacity_cc", "oil_filter_age_days", "km_after_change",
    "avg_oil_temperature", "oil_viscosity_index", "engine_rpm_avg",
    "idling_percentage", "ambient_temperature"
]

cat_cols = [
    "vehicle_type", "road_type", "load_type",
    "fuel_type", "driving_style"
]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
    ]
)

# ---------------------------------------------------------
# 5. Define model
# ---------------------------------------------------------
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=None,
    class_weight="balanced",
    random_state=42
)

# ---------------------------------------------------------
# 6. Create pipeline (Preprocessing + Model)
# ---------------------------------------------------------
pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("classifier", model)
])

# ---------------------------------------------------------
# 7. Train the model
# ---------------------------------------------------------
pipeline.fit(X_train, y_train)

print("\nModel training completed successfully!")

# ---------------------------------------------------------
# 8. Evaluate the model
# ---------------------------------------------------------
y_pred = pipeline.predict(X_test)

print("\n================ MODEL EVALUATION ================")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# ---------------------------------------------------------
# 9. Save trained model for Streamlit deployment
# ---------------------------------------------------------
joblib.dump(pipeline, "oil_filter_model.pkl")

print("\nModel saved as 'oil_filter_model.pkl'")
