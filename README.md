# ❤️ Heart Disease Prediction Web App

A Machine Learning powered web application that predicts the risk of heart disease based on patient health parameters. Built using **Logistic Regression** and deployed with **Streamlit**.

---

## 🚀 Live Demo

👉 *(Add your deployed app link here)*

---

## 📌 Project Overview

This project aims to predict whether a person is at risk of heart disease using medical attributes such as age, cholesterol, blood pressure, and more.

It includes:

* Data preprocessing & cleaning
* Feature engineering (encoding + scaling)
* Model training & evaluation
* Interactive web UI using Streamlit

---

## 🧠 Machine Learning Model

* **Algorithm Used:** Logistic Regression
* **Accuracy:** ~87%
* **Evaluation Metrics:**

  * Precision
  * Recall
  * F1-Score
  * Confusion Matrix

---

## 📊 Features Used

* Age
* Gender (IsFemale)
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Max Heart Rate
* Exercise Induced Angina
* Oldpeak
* Chest Pain Type (Encoded)
* Resting ECG (Encoded)
* ST Slope (Encoded)

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Matplotlib & Seaborn
* Joblib

---

## 📁 Project Structure

```
heart-disease-prediction/
│
├── app.py                # Streamlit UI
├── heart_model.pkl       # Trained ML model
├── scaler.pkl            # Feature scaler
├── requirements.txt      # Dependencies
├── heart.csv             # Dataset (optional)
└── README.md             # Project documentation
```

---

## 🛠️ Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/YOUR_USERNAME/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run the App

```
streamlit run app.py
```

---

## 📈 How It Works

1. User inputs health details in the UI
2. Data is preprocessed (encoding + scaling)
3. Model predicts heart disease risk
4. Result is displayed with probability

---

## ⚠️ Important Notes

* Cholesterol values of 0 were treated as missing and replaced
* Scaling applied only to numerical features
* Feature order strictly maintained for predictions

---

## 🎯 Future Improvements

* Add SHAP for model explainability
* Improve UI/UX design
* Add user authentication
* Deploy using Docker

---

## 👨‍💻 Author

**Harsh Kumar**
🚀 Aspiring Data Scientist

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!
