import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
import joblib

print("Loading training data...")
train = pd.read_csv('cs-training.csv')

print("Preprocessing data...")
# Fill missing MonthlyIncome with median
MonthlyIncome_imputer = SimpleImputer(strategy='median')
train['MonthlyIncome'] = MonthlyIncome_imputer.fit_transform(train[['MonthlyIncome']])

# Fill missing NumberOfDependents with median
train["NumberOfDependents"] = train["NumberOfDependents"].fillna(train["NumberOfDependents"].median())

# Separate features and target
X = train.drop(columns=['Unnamed: 0', 'SeriousDlqin2yrs'])
y = train['SeriousDlqin2yrs']

print("Training HistGradientBoostingClassifier model...")
# Using parameters from the notebook or default values for a strong baseline
model = HistGradientBoostingClassifier(
    max_iter=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)

model.fit(X, y)
print("Training complete.")

model_filename = "model.joblib"
print(f"Saving model to {model_filename}...")
joblib.dump(model, model_filename)

print("Model saved successfully. Ready for Streamlit!")
