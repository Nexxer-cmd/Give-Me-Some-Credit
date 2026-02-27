🚀 Credit Risk Predictor
AI-Powered Loan Default Risk Assessment System

A production-ready machine learning web application that predicts the probability of a borrower defaulting within the next two years.

📌 Introduction

Lending decisions are high-stakes. Even small miscalculations in credit risk assessment can lead to significant financial losses.

This project delivers an interactive AI-powered Credit Risk Prediction system built with:

🧠 Machine Learning (HistGradientBoostingClassifier)

🌐 Streamlit (Premium UI with multi-step risk wizard)

📊 Altair (Interactive data insights)

🗃️ Robust preprocessing & model serialization

The system enables financial institutions (or analysts) to:

Evaluate borrower risk in real-time

Explore historical dataset insights

Understand the architecture behind the AI engine

📖 Table of Contents

Project Overview

System Architecture

Features

Installation

Usage

Model Training

Dependencies

Project Structure

Data Insights Dashboard

Example Output

Troubleshooting

Future Improvements

License

🎯 Project Overview

The application predicts the probability that a borrower will experience serious delinquency (90+ days past due) within two years.

🎯 Target Variable:

SeriousDlqin2yrs

🔍 Key Risk Factors Used:

Revolving Utilization of Unsecured Lines

Age

Debt Ratio

Monthly Income

Delinquency History (30–59, 60–89, 90+ days late)

Number of Open Credit Lines

Real Estate Loans

Number of Dependents

🏗 System Architecture
Dataset (cs-training.csv)
        ↓
Data Cleaning & Median Imputation
        ↓
HistGradientBoostingClassifier
        ↓
Model Serialization (model.joblib)
        ↓
Streamlit Web App
        ↓
User Risk Prediction + Dashboard Insights
🧠 Model

The system uses:

HistGradientBoostingClassifier(
    max_iter=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)

Why this model?

Optimized for large tabular datasets

Handles missing values efficiently

Strong performance baseline

Faster than traditional Gradient Boosting

✨ Features
🧭 1. Multi-Step Risk Assessment Wizard

Clean, premium UI

Step-by-step borrower profiling

Animated risk indicator

Risk classification tiers:

🟢 Excellent Profile (<10%)

🟡 Moderate Risk (10–30%)

🔴 High Risk (>30%)

📊 2. Data Insights Dashboard

Explore:

Age distribution vs default rates

Income vs debt ratio scatter plots

Default rate baseline

Raw dataset viewer

Built using Altair interactive visualizations.

🏛 3. System Architecture Page

Explains:

Problem statement

AI engine

Predictive factors

Technology stack

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/credit-risk-predictor.git
cd credit-risk-predictor
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies

Dependencies are defined in requirements.txt

pip install -r requirements.txt
▶️ Usage
Run the Streamlit Application
streamlit run app.py

The application will launch locally in your browser.

🧠 Model Training

Training script: train.py

To retrain the model:

Place cs-training.csv in the root directory.

Run:

python train.py

This will:

Load dataset

Apply median imputation

Train HistGradientBoostingClassifier

Save model as:

model.joblib
📦 Dependencies

From requirements.txt :

pandas
scikit-learn
joblib
streamlit

Optional (used in app):

altair
📁 Project Structure
credit-risk-predictor/
│
├── app.py                 # Streamlit Web Application
├── train.py               # Model training script
├── model.joblib           # Trained ML model
├── requirements.txt       # Project dependencies
├── cs-training.csv        # Training dataset (not included)
├── Data Dictionary.xls    # Feature descriptions
└── project.ipynb          # Experimental notebook
📊 Data Insights Dashboard

The dashboard provides:

📈 Age vs Default Distribution

💰 Income vs Debt Ratio Scatter Plot

📉 Baseline Default Rate

🔍 Sample dataset preview

It loads a sample (10,000 rows) for performance optimization.

📌 Example Output
Input:

Age: 35

Monthly Income: $5,000

Debt Ratio: 0.4

No severe delinquency history

Output:
Calculated Default Probability: 8.7%
Risk Level: Excellent Profile
🛠 Troubleshooting
❗ Model fails to load

Ensure:

model.joblib exists in root directory

You trained the model successfully

❗ Dataset not loading in dashboard

Ensure:

cs-training.csv is present

File name matches exactly

❗ Module not found error

Reinstall dependencies:

pip install -r requirements.txt
🔮 Future Improvements

Model explainability (SHAP values)

Authentication system for lenders

Docker containerization

API endpoint version

Model performance metrics dashboard

Cloud deployment (AWS/GCP/Azure)

👨‍💻 Contributors

Developed as a Machine Learning risk assessment system project.

📜 License

This project is intended for educational and demonstration purposes.
