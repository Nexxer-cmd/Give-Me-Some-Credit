# 🚀 Credit Risk Predictor  
### AI-Powered Loan Default Risk Assessment System  

An end-to-end Machine Learning web application that predicts the probability of a borrower defaulting within the next two years.

Built with:
- 🧠 Scikit-Learn (HistGradientBoostingClassifier)
- 🌐 Streamlit (Interactive Web Interface)
- 📊 Altair (Data Visualization)
- 💾 Joblib (Model Serialization)

---

## 📌 Overview

This project provides a production-style credit risk prediction system that:

- Assesses borrower default risk in real-time
- Visualizes historical credit data trends
- Demonstrates a full ML pipeline (training → deployment)

The model predicts the likelihood of **Serious Delinquency (90+ days past due)** within 2 years.

---

## 🎯 Target Variable

`SeriousDlqin2yrs`

Binary classification:
- `0` → No serious delinquency
- `1` → Serious delinquency within 2 years

---

## 🏗 System Architecture

```
Dataset (cs-training.csv)
        ↓
Data Cleaning & Imputation
        ↓
HistGradientBoostingClassifier
        ↓
Model Serialization (model.joblib)
        ↓
Streamlit Web Application
        ↓
Live Risk Prediction
```

---

## ✨ Features

### 1️⃣ Risk Assessment Wizard
- Multi-step borrower profiling
- Clean premium UI
- Real-time risk scoring
- Visual probability indicator
- Risk categories:
  - 🟢 Excellent (<10%)
  - 🟡 Moderate (10–30%)
  - 🔴 High (>30%)

---

### 2️⃣ Data Insights Dashboard
- Age distribution analysis
- Default rate by age group
- Income vs Debt Ratio scatter plot
- Baseline default rate
- Interactive dataset preview

---

### 3️⃣ Model Transparency Page
- Problem statement explanation
- Key predictive features
- Technology stack overview

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/credit-risk-predictor.git
cd credit-risk-predictor
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

The app will open in your default browser.

---

## 🧠 Training the Model

To retrain the model:

1. Place `cs-training.csv` in the project root.
2. Run:

```bash
python train.py
```

This will:
- Clean missing values
- Train the HistGradientBoostingClassifier
- Save the model as `model.joblib`

---

## 📦 Dependencies

```
pandas
scikit-learn
joblib
streamlit
```

(Optional for visualization)
```
altair
```

---

## 📁 Project Structure

```
credit-risk-predictor/
│
├── app.py                 # Streamlit Web Application
├── train.py               # Model training script
├── model.joblib           # Trained ML model
├── requirements.txt       # Dependencies
├── cs-training.csv        # Dataset (not included)
├── Data Dictionary.xls    # Feature descriptions
└── project.ipynb          # Experimental notebook
```

---

## 📊 Example Prediction

**Input:**
- Age: 35  
- Monthly Income: $5,000  
- Debt Ratio: 0.4  
- No severe delinquency  

**Output:**
```
Default Probability: 8.7%
Risk Level: Excellent Profile
```

---

## 🛠 Troubleshooting

### Model not loading?
Ensure `model.joblib` exists in the root directory.

### Dataset not showing in dashboard?
Ensure `cs-training.csv` is in the same directory.

### Missing modules?
Run:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

- SHAP model explainability
- Docker containerization
- REST API deployment
- Cloud hosting (AWS / GCP)
- Model performance metrics dashboard
- User authentication system

---

## 📜 License

This project is for educational and demonstration purposes.

---

## 🌟 Why This Project Matters

This project demonstrates:
- End-to-end ML deployment
- Financial risk modeling
- Clean UI/UX design
- Production-style architecture
- Real-world business application

---

Built with ❤️ using Python and Machine Learning.
