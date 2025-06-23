# 🩺 Healthcare Cyber Threat Intelligence Analysis

This project collects, explores, and models cyber threat data related to healthcare breaches, sourced from the HIPAA Journal. The aim is to uncover trends in healthcare data breaches and predict the number of individuals affected using machine learning.

---

## 🔍 Project Overview

**Source**  
Scraped breach data from the [HIPAA Journal](https://www.hipaajournal.com/) using:
- `Selenium` with `Chromedriver` to handle JavaScript-rendered content
- `BeautifulSoup` to parse and extract data from HTML

**Objectives**
- Extract healthcare breach data into a clean CSV
- Visualize breach patterns across states, years, and entity types
- Predict breach impact (number of individuals affected) using regression

---

## 🛠️ Tools & Technologies

- **Web Scraping**: Selenium, Chromedriver, BeautifulSoup  
- **Data Analysis & Visualization**: Pandas, Matplotlib, Seaborn  
- **Machine Learning**: XGBoost Regressor (XGBRegressor), Scikit-learn

---

## 🗂️ Project Structure
data/ — Datasets (raw or cleaned)

healthcare_breaches.csv — Scraped breach data from HIPPA Journal

notebooks/ — Jupyter notebooks for analysis

healthcare data.ipynb — Web scraping from HIPAA Journal

Healthcare_Breaches.ipynb — EDA and visualizations

src/ — Python scripts

regression_model.py — Script for training and evaluating the model

visualizations/ — Output plots and charts

heatmap.png — Breaches by state and year

pie_chart.png — Covered Entity Type distribution

README.md — Project overview and documentation


---

## 📁 Dataset

**Filename**: `healthcare_breaches.csv`

**Columns**:
- `State`
- `Covered Entity Type`
- `Type of Breach`
- `Individuals Affected`
- `Year`

**Preprocessing**:
- Handled missing values
- Ensured proper data types

---

## 📊 Exploratory Data Analysis

Two key visualizations were created:

1. **Heatmap**  
   Shows the number of breaches by state and year  
   *(See: `heatmap.png` in visualizations)*

2. **Pie Chart**  
   Displays the distribution of Covered Entity Types  
   *(See: `pie_chart.png` in visualizations)*

---

## 🤖 Predictive Modeling

A regression model was developed to predict the number of individuals affected by a breach.

- **Features**: `State`, `Covered Entity Type`, `Type of Breach`, `Year`
- **Target**: `Individuals Affected` (log-transformed)
- **Model**: `XGBRegressor`

**Model Performance**:
- **MSE**: 2.24  
- **RMSE**: 1.50  
- **MAE**: 0.93  
- **R² Score**: -0.87 (Baseline: 1.34)

⚠️ *The model had poor generalization, reflecting the complexity of breach severity prediction using only metadata.*

---

## 📌 Key Takeaways

- **Business Associates** are involved in over **50%** of breach incidents.
- Breach frequency fluctuates significantly by **state** and **year**.
- Predicting the number of affected individuals is complex and likely requires richer context.

---

## ✅ Future Improvements

- Add granular features (e.g., breach description, duration, resolution time)
- Explore classification models (e.g., high vs low impact breaches)
- Integrate with external threat intelligence sources
- Essentially, the dataset is too small








