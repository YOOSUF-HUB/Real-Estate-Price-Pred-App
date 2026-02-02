# 🏡 AI Real Estate Price Predictor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Model-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A machine learning-powered web application that predicts residential house prices based on the **Ames Housing Dataset**. The app features a Flask backend serving a Random Forest Regressor model and a modern, responsive "Glassmorphism" user interface.

## 📸 Demo
*(Optional: Insert a screenshot of your beautiful UI here)*
## 🚀 Features
* **Machine Learning Model:** Utilizes a Random Forest Regressor trained on the Ames Housing dataset (80+ features originally, optimized to top 12 drivers of price).
* **High Accuracy:** The model achieves an **R² Score of ~0.91** on test data.
* **Modern UI:** A responsive, glass-effect interface built with HTML5, CSS3, and JavaScript.
* **Real-time Prediction:** Instant feedback via a RESTful Flask API.

## 🛠️ Tech Stack
* **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript (Fetch API)
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Serialization:** Joblib

## 📂 Project Structure
```text
HousePriceApp/
│
├── model/
│   ├── training_notebook.ipynb  # Jupyter Notebook used for training
│   └── ames_housing_model.pkl   # Serialized Machine Learning Model
│
├── templates/
│   └── index.html               # Frontend User Interface
│
├── app.py                       # Flask Application Entry Point
├── requirements.txt             # Project Dependencies
└── README.md                    # Project Documentation
