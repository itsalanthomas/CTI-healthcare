🩺 Healthcare Cyber Threat Intelligence Analysis
This project focuses on collecting, exploring, and modeling cyber threat data related to healthcare breaches, sourced from the HIPAA Journal. The goal is to understand patterns in breach incidents and predict the number of individuals affected by such events using machine learning.

🔍 Project Overview
Source: Data was scraped from HIPAA Journal using Selenium (Chromedriver) to handle JavaScript-rendered content, in conjunction with BeautifulSoup for parsing HTML.

Goal:

Extract healthcare breach data into a clean, structured CSV.

Explore and visualize trends across states, time, and breach types.

Predict the impact of future breaches by modeling the number of individuals affected.

🛠️ Tools & Technologies
Web Scraping: Selenium, Chromedriver, BeautifulSoup

Data Analysis & Visualization: Pandas, Matplotlib, Seaborn

Machine Learning: XGBoost Regressor (XGBRegressor), Scikit-learn

📁 Dataset
File: healthcare_breaches.csv

Fields include:

State

Covered Entity Type

Type of Breach

Individuals Affected

Year

Preprocessing included:

Handling missing/null values

Ensuring appropriate data types for modeling

📊 Exploratory Data Analysis
Two main visualizations were created:

Heatmap:
Visualizing the number of healthcare breaches per state and year

Pie Chart:
Showing the distribution of Covered Entity Types involved in breaches

🤖 Predictive Modeling
A regression model was trained to predict the number of individuals affected by a breach using:

Features: State, Covered Entity Type, Type of Breach, and Year

Target: Individuals Affected (log-transformed)

Model: XGBRegressor
Metrics:

MSE: 2.24

RMSE: 1.50

MAE: 0.93

R² Score: -0.87 (baseline: 1.34)

Although model performance was limited, this highlights the variability and potential complexity in predicting breach impact based on metadata alone.

📌 Key Takeaways
Business Associates are involved in over 50% of breach cases.

Breach frequency varies widely by state and year.

Modeling breach impact is challenging and may require more granular features (e.g., breach size, incident response time, data type exposed).

✅ Future Improvements
Include more granular breach attributes (e.g., detailed descriptions, resolution times).

Explore classification models (e.g., high vs low impact breaches).

Integrate external threat intelligence or vendor datasets.

