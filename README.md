# dsa210-project
# DSA 210 – Introduction to Data Science

**Name:** Kemal Yağız Uludağ  
**Student ID:** 34309  

---

## Project Overview

This project focuses on understanding customer purchasing behavior and identifying whether early transaction patterns can be used to predict high-value customers.

In e-commerce, businesses typically recognize valuable customers only after they have already generated significant revenue. This project aims to take a proactive approach by analyzing early-stage customer behavior to determine whether future high-value customers can be identified in advance.

---

## Research Question

Can early customer purchasing behavior be used to predict high-value customers before they fully emerge?

---

## Data Source

The project uses a publicly available dataset:

- Online Retail II Dataset (UCI Machine Learning Repository)  
- Over 500,000 transaction records  

The dataset includes:
- Customer ID  
- Purchase date  
- Quantity  
- Unit price  

---

## Methodology

The project follows a structured data science pipeline:

1. Data Collection  
   The Online Retail II dataset was used as the primary data source.

2. Data Cleaning  
   - Removed missing values  
   - Filtered out transactions with negative quantities and prices  
   - Created a new variable: TotalPrice  

3. Feature Engineering  
   - Aggregated data at the customer level  
   - Frequency: number of unique purchases  
   - Monetary: total spending per customer  

4. Exploratory Data Analysis (EDA)  
   - Examined the distribution of customer purchasing behavior  
   - Identified strong skewness in frequency distribution  
   - Compared high-value and low-value customers  

5. Hypothesis Testing  
   - Used Mann-Whitney U test  
   - Tested whether high-value customers differ significantly in purchase frequency  

6. Future Work (Machine Learning)  
   - Build classification models to predict high-value customers  
   - Potential models: Logistic Regression, Random Forest  

---

## Goal

The goal of this project is to:

- Identify behavioral patterns of high-value customers  
- Build a predictive model for early customer value classification  
- Generate actionable insights for business decision-making  

---

## Tools

- Python (Pandas, NumPy, Scikit-learn)  
- Data visualization (Matplotlib, Seaborn)  
- Jupyter Notebook  


## Results

The Mann-Whitney U test yielded a p-value of 0.0, indicating a statistically significant difference in purchase frequency between high-value and low-value customers.

This confirms that purchase frequency is a strong indicator of customer value.

Additionally, exploratory data analysis showed that customer purchase behavior is highly skewed, with a small group of customers contributing disproportionately to overall activity.

High-value customers consistently exhibit higher purchase frequency, suggesting that frequency can serve as a strong early signal for identifying valuable customers.

---

## Machine Learning Modeling

To extend the analysis beyond hypothesis testing, machine learning models were applied to predict high-value customers based on early purchasing behavior.


The consistency between hypothesis testing and machine learning results strengthens the validity of the findings. Both approaches indicate that early customer behavior contains strong signals for identifying high-value customers.

### Model Setup

- Features:
  - EarlyFrequency
  - EarlyMonetary
  - EarlyQuantity
  - EarlyUniqueProducts
  - EarlyAvgOrderValue

- Target:
  - HighValue (top 20% of customers based on total spending)

The dataset was split into training and testing sets using an 80/20 ratio, with stratification to preserve class distribution.

### Models Used

1. Logistic Regression  
   - Used as a baseline model  
   - Interpretable but limited in capturing complex relationships  

2. Random Forest  
   - Nonlinear model capable of capturing more complex patterns  
   - Provided improved performance over Logistic Regression  

### Evaluation

Due to class imbalance, accuracy alone is not sufficient. Therefore, the following metrics were considered:

- Precision  
- Recall  
- F1-score  

The results show that:

- Logistic Regression struggled to identify high-value customers because of relatively low recall  
- Random Forest improved recall and captured more high-value customers  

### Feature Importance

Feature importance analysis from the Random Forest model revealed that:

- EarlyMonetary is the most important predictor  
- EarlyQuantity and EarlyAvgOrderValue also contribute significantly  
- EarlyFrequency has relatively lower importance  

This suggests that how much a customer spends early is more important than how often they purchase.

### Key Insight

High-value customers can be identified early in their lifecycle, primarily based on their initial spending behavior rather than purchase frequency alone.

This insight is valuable for businesses aiming to target valuable customers early with personalized strategies.

### Model Performance Interpretation

The results indicate that while both models perform reasonably well in identifying low-value customers, detecting high-value customers remains more challenging.

Logistic Regression achieves high overall accuracy but suffers from low recall, meaning it fails to identify a significant portion of high-value customers.

Random Forest improves recall, successfully identifying more high-value customers, although with a slight increase in false positives.

This trade-off is acceptable in business contexts where missing a high-value customer is more costly than incorrectly targeting a low-value one.

Therefore, Random Forest is considered the more effective model for this problem. 