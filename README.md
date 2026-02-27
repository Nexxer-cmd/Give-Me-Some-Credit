💳 Credit Default Risk Prediction System

A production-style Machine Learning web application that predicts the probability of a borrower defaulting on a loan within the next two years.

Built using Streamlit, Scikit-Learn, and HistGradientBoostingClassifier, this system provides:

📊 Interactive risk assessment

📈 Data exploration dashboard

🧠 ML-based probability scoring

🎨 Clean, premium UI experience

🚀 Live Features
1️⃣ Risk Assessment System

A 3-step guided assessment form that collects:

Personal & income details

Credit utilization metrics

Delinquency history

The model returns:

✅ Default probability (%)

🟢 Risk category (Excellent / Moderate / High)

📊 Visual risk indicator bar

2️⃣ Data Insights Dashboard

Explore a sample of the historical training dataset:

Age distribution analysis

Default rate by age group

Income vs debt ratio scatter plot

Interactive data table preview

3️⃣ System Architecture View

Explains:

Problem statement

ML model design

Key predictive factors

Technology stack

🧠 Machine Learning Model

Algorithm: HistGradientBoostingClassifier

Target Variable: SeriousDlqin2yrs

Problem Type: Binary Classification

Objective: Predict probability of default within 2 years

Key Predictive Features:

Revolving Utilization of Unsecured Lines

Number of 30/60/90 day past dues

Debt Ratio

Monthly Income

Open credit lines

Real estate loans

Age

Number of dependents

🏗️ Project Structure
📂 Project Root
│
├── app.py
├── model.joblib
├── cs-training.csv
├── project.ipynb
├── Data Dictionary.xls
├── requirements.txt
└── README.md

app.py → Streamlit application 

app

project.ipynb → Model training & experimentation notebook

requirements.txt → Dependencies 

requirements

Data Dictionary.xls → Feature descriptions

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/credit-risk-predictor.git
cd credit-risk-predictor
2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt

Dependencies include:

pandas

scikit-learn

joblib

streamlit 

altair

requirements

4️⃣ Run the Application
streamlit run app.py
📊 Dataset

The dataset used is the Give Me Some Credit dataset.

Target variable:

SeriousDlqin2yrs

Binary indicator:

1 → Borrower experienced serious delinquency

0 → No serious delinquency

🎯 Business Value

This system can help:

🏦 Banks reduce credit risk

💳 Fintech companies automate risk scoring

📉 Minimize loan defaults

⚡ Speed up underwriting decisions

🔐 Model Output Interpretation
Probability	Risk Level
< 10%	Excellent Profile
10% – 30%	Moderate Risk
> 30%	High Risk
🛠️ Tech Stack
Layer	Technology
Frontend	Streamlit
Visualization	Altair
Backend	Python
ML Framework	Scikit-Learn
Model Storage	Joblib
📈 Future Improvements

Add SHAP explainability

Deploy to Streamlit Cloud / AWS

Add model monitoring dashboard

Include SMOTE-based retraining pipeline

Add user authentication layer

👨‍💻 Author

Developed as a full-stack ML portfolio project demonstrating:

End-to-end ML pipeline

Model deployment

UI/UX engineering

Data visualization

Financial risk modeling
