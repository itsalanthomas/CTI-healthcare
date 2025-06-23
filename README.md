🩺 Healthcare Cyber Threat Intelligence Analysis

This project focuses on collecting, exploring, and modeling cyber threat data related to healthcare breaches, sourced from the HIPAA Journal. The goal is to uncover breach trends and predict the number of individuals affected using machine learning.

🔍 Project Overview
Source
Data was scraped from the HIPAA Journal using:

Selenium (with Chromedriver) for rendering JavaScript-based content

BeautifulSoup for parsing and extracting HTML elements

Objectives

Extract healthcare breach data into a clean, structured CSV

Explore and visualize trends across states, years, and breach types

Predict the potential impact of future breaches via regression modeling

🛠️ Tools & Technologies
Web Scraping: Selenium, Chromedriver, BeautifulSoup

Data Analysis & Visualization: Pandas, Matplotlib, Seaborn

Machine Learning: XGBoost Regressor (XGBRegressor), Scikit-learn

📁 Dataset
File: healthcare_breaches.csv

Key Columns:

State

Covered Entity Type

Type of Breach

Individuals Affected

Year

Preprocessing Steps:

Handled missing and null values

Converted columns to appropriate data types for analysis and modeling

📊 Exploratory Data Analysis
Two core visualizations were created to examine trends:

Heatmap
Number of healthcare breaches by state and year
📎 heatmap.png

Pie Chart
Distribution of Covered Entity Types involved in breaches
📎 pie_chart.png

🤖 Predictive Modeling
A regression model was built to predict the number of individuals affected by a breach using:

Features: State, Covered Entity Type, Type of Breach, Year

Target: Individuals Affected (log-transformed)

Model Used: XGBRegressor

Performance Metrics:

MSE: 2.24

RMSE: 1.50

MAE: 0.93

R² Score: -0.87 (Baseline: 1.34)

⚠️ The model struggled to generalize, revealing the complexity and high variance in predicting breach impact based on metadata alone.

📌 Key Takeaways
Business Associates accounted for over 50% of breach cases.

Breach activity varies significantly by state and year.

Accurate prediction of breach impact likely requires more detailed features, such as:

Data type exposed

Resolution time

Breach scope or narrative descriptions

✅ Future Improvements
Incorporate additional breach-level attributes (e.g., detailed descriptions, response time).

Test classification models for predicting high-impact vs low-impact breaches.

Enrich the dataset using external cyber threat intelligence or vendor metadata.

