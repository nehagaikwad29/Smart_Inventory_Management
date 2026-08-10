# 🤖 Smart Inventory Management

## 📌 Project Overview

Smart Inventory Management is an Artificial Intelligence and Machine Learning based system designed to predict future product demand and provide intelligent inventory recommendations.

The system uses historical sales data and a Machine Learning model to predict product demand. Based on the predicted demand and current stock, it also provides inventory status and smart reorder recommendations.

The project also includes an interactive Streamlit web application that allows users to enter store, product, date, and recent sales information and generate demand predictions.

---

## 🎯 Objectives

- Predict future product demand using Machine Learning.
- Analyze current inventory levels.
- Identify inventory status.
- Calculate recommended reorder quantity.
- Reduce the risk of stock shortages and overstocking.
- Provide an interactive and user-friendly web application.
- Support data-driven inventory management decisions.

---

## 📊 Dataset

The project uses a demand forecasting dataset containing historical sales data for stores and products.

### Key Features

- Store ID
- Product ID
- Date
- Historical Sales
- Year
- Month
- Day
- Day of Week
- Lag 1
- Lag 7

### Target Variable

**Product Sales / Demand**

### Dataset Source

The dataset is a demand forecasting dataset containing historical sales information for different stores and products.

The dataset is used to analyze historical demand patterns and build a Machine Learning model for demand prediction.

---

## 🧹 Data Preprocessing and Feature Engineering

The following preprocessing and feature engineering steps were performed:

- Checked for missing values.
- Checked for duplicate records.
- Converted date information into a proper date format.
- Extracted Year, Month, Day, and Day of Week from the date.
- Created lag-based features for historical demand.
- Created **Lag 1**, representing previous day sales.
- Created **Lag 7**, representing sales from seven days earlier.
- Prepared the dataset for Machine Learning.
- Used a time-based train-test split to maintain the chronological order of the data.

---

## 🔍 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the sales and demand patterns in the dataset.

The analysis includes:

- Dataset structure and summary statistics.
- Missing-value analysis.
- Duplicate-value analysis.
- Sales and demand patterns.
- Feature relationships.
- Model feature importance.
- Actual vs predicted demand visualization.
- Prediction error analysis.

---

## 🤖 Machine Learning Algorithm

### Random Forest Regressor

Random Forest Regressor was selected as the main Machine Learning algorithm because the project is a regression problem where the target variable is a continuous numerical value.

Random Forest can capture complex and nonlinear relationships between different features and product demand.

### Model Input Features

The final Random Forest model uses the following eight features:

```text
store
item
year
month
day
day_of_week
lag_1
lag_7
