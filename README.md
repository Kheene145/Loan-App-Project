# Loan Approval App

## Table of Contents
- [Project Overview](#project-overview)
- [Data Source](#data-source)
- [Tools](#tools)
- [Data Cleaning Preparation](#data-cleaning-preparation)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Data Analysis](#data-analysis)
- [Results](#results)
- [Recommendations](#recommendations)
- [Limitation](#limitations)
- [References](#references)

### Project Overview
---



- [Dashboard](bar plot.PNG)
- 
![Bar plot](https://github.com/user-attachments/assets/ea652baf-4901-4a0f-b138-0844b511770f)



### Data Source
The primary data source for this project is the "Rides_Data.csv", containing detailed information made by the company(CityRide)

### Tools
- Jupyter Notebook - Data cleaning and exploration
  - [Download here](https://jupyter.org)


### Data Cleaning/Preparation
In the initail data preparation phase, we performed the following taskes:
1. Data loading & Inspection.
2. Handing missing values & duplicates.
3. Data cleaning & formatting.


### Exploratory Data Analysis
- What are the total earning per driver or across the entire dataset?
- Which ride generate the most revenue? By distance and duration ?
- How does ride rating correlate with fare and ride duration?
- Can we predict a fare base on ride distance and duration?
- What is the average fare per kilometer or minute, and how does it vary


### Data Analysis
Include some interesting codes/features worked with.

```jupyter notebook
df_cityride.head()
```

### Result/Findings
The analysis result are summarized as follows
- Insight into the fare-per minute and fare-per-kilometer values can help optimize driver incentives by focusing on the most profitable ride types or duration
- Regional or temporal differences in fare data can guide strategic pricing adjustments, helping to maintain competitiveness and expand into new market effcetively.
- Driver with consitently low ratings and poor performance were identified, providing opportunities for targeted training or performance improvement strategies.
- The average fare per kilometer and per minute provide a baseline for evaluating the pricing structure. Consistent averages suggest a stable pricing model, while high variation indicates potential inefficiencies.
- A regressive model indicated the ability to predict ride fares based on ride distance and duration, providing a foundation for implementing dynamic pricing strategies or forecasting revenue. 


### Recommendations

- Address low performing drivers throughtargeted training and incentives to improve ratings and productivity
- Implementing dynamic pricing strategies based on fare analysis to maximize profitability and ensure competitive pricing.
- Enhance customer experience by leveraging ride ratings and offering loyalty rewards to boost satisfaction and retention.
- Use predictive analytics to forecast fares accurately and optimize pricing transparency
- Focus operational effots on high-revenue areas and routes, while investigatingoutliers to identify and correct inefficiencies.


  ### Limitations
  The dataset lacks contextual variables like time of the day, traffic conditions or geographical information, limiting deeper insights into operational factors. Additionally, the absence of customer feedback data restrict s the abilit to fully assess customer satisfaction and experince.



### References
1. [Kaggle.com](https://www.kaggle.com/datasets/rishabhrajsharma/cityride-dataset-rides-data-drivers-data?resource=download&select=Rides_Data.csv)
2. Python libraries such as:
   - Pandas
   - Matplotlib
   - Seaborn
   - scikit-learn


😄

💻
  
