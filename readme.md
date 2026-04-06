# 🏠 Smart Property Advisor

## 📌 Overview

Smart Property Advisor is a machine learning–based web application designed to assist users in evaluating real estate properties. It combines predictive analytics with decision-support insights to estimate property prices, assess investment potential, and provide actionable recommendations.

The system analyzes multiple factors such as property characteristics, location quality, amenities, and neighborhood conditions to deliver a comprehensive evaluation of a property.

---

## 🎯 Objectives

* Predict property prices based on key features
* Evaluate investment potential using a scoring system
* Provide intelligent recommendations for better decision-making
* Help users minimize risks in real estate investments

---

## ⚙️ Features

### 💰 Price Prediction

Estimates property price using a trained machine learning model based on:

* Area (sqft)
* Number of bedrooms and bathrooms
* Property type
* Location tier
* Distance to city center

---

### 📊 Investment Score

Calculates a score (0–100) indicating the investment quality of a property by considering:

* Crime rate
* School ratings
* Accessibility (distance to hospitals, shopping centers)
* Location advantages

---

### 💡 Smart Recommendations

Provides personalized suggestions such as:

* Improving amenities (garden, pool, furnishing)
* Identifying risk factors (high crime areas)
* Highlighting growth potential of locations

---

### 🎛 Interactive Dashboard

* User-friendly interface built with Streamlit
* Sidebar navigation for easy interaction
* Visual indicators like gauge charts for investment score

---

## 🧠 Machine Learning Model

* Algorithm: Random Forest Regressor
* Handles nonlinear relationships between features
* Trained on a structured dataset representing real estate attributes

---

## 📂 Dataset

This project uses a **synthetic dataset** (`smart_property_data.csv`) created to simulate real-world real estate conditions.

### Dataset Features:

* Property details: sqft, bedrooms, bathrooms, floor, age
* Location factors: location tier, distance to city center
* Amenities: garden, pool, garage, furnished
* Neighborhood metrics: crime rate, school rating, hospital & shopping distance
* Target: property price

---

## 🛠 Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Plotly

---

## 🚀 How to Run the Project

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
streamlit run app.py
```

---

## 📈 Use Cases

* Property buyers comparing options
* Real estate investors analyzing potential returns
* Students and researchers exploring ML applications in real estate

---

## ⚠️ Limitations

* Uses a small synthetic dataset
* Model accuracy is limited due to dataset size
* Does not include real-time market data

---

## 🔮 Future Enhancements

* Integration with real-world datasets
* Advanced models (XGBoost, Deep Learning)
* Location-based mapping (GIS integration)
* User authentication and saved predictions
* Model performance metrics and explainability

---

## 📌 Conclusion

Smart Property Advisor demonstrates how machine learning can be applied to real estate decision-making. It provides users with meaningful insights beyond price prediction, making it a useful tool for evaluating property investments.

---