# Smart Inventory Management

## 📌 Project Overview

Smart Inventory Management is an Artificial Intelligence and Machine Learning based system designed to predict future product demand and provide intelligent inventory recommendations.

The system uses historical sales data and a Machine Learning model to predict demand. Based on the predicted demand and current stock, it also provides inventory status and smart reorder recommendations.

## 🎯 Objectives

- Predict future product demand using Machine Learning.
- Analyze current inventory levels.
- Identify inventory status.
- Calculate recommended reorder quantity.
- Reduce the risk of stock shortages and overstocking.
- Provide an interactive and user-friendly web application.

## 📊 Dataset

The project uses a demand forecasting dataset containing historical product sales information.

### Key Features

- Store ID
- Product ID
- Date
- Historical Sales
- Year
- Month
- Day
- Day of Week

### Target Variable

**Product Sales / Demand**

## 🤖 Machine Learning Algorithm

### Random Forest Regressor

Random Forest Regressor was selected as the main Machine Learning algorithm because the project is a regression problem where the target variable is a continuous numerical value.

Random Forest can capture complex and nonlinear relationships between different features and product demand.

## 📈 Model Performance

The final Random Forest model achieved the following results:

| Evaluation Metric | Result |
|---|---:|
| MAE | 7.40 |
| RMSE | 9.61 |
| R² Score | 0.9072 |
| R² Performance | 90.72% |

### Result Interpretation

**MAE – 7.40:**  
The model's predictions differ from the actual demand by approximately 7.40 units on average.

**RMSE – 9.61:**  
RMSE measures prediction error while giving greater importance to larger errors.

**R² Score – 0.9072:**  
The model explains approximately 90.72% of the variation in product demand.

## ⭐ Key Features

### 🔮 Demand Prediction

Predict
