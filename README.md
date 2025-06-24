# 🧠 Trader Behavior Insights

This project analyzes how trader performance correlates with market sentiment using historical trading data and the Fear-Greed Index.


- **Goal:** Understand how trader behavior changes under different market sentiments (Fear, Neutral, Greed).
- **Data Used:**  
  - Historical trading data (`historical_data.csv`)  
  - Fear & Greed Index (`fear_greed_index.csv`)

- Merged trader data with sentiment index by date
- Cleaned and standardized fields like `timestamp`, `closedPnL`, `leverage`, `win`

-  Win rate comparison under Fear vs Greed
-  Leverage behavior by sentiment
-  Time-of-day impact on win rate
-  Account-level analysis for overtrading
-  Optional: Logistic Regression to predict profitable trades

- Traders tend to use **higher leverage during Greed**, but not always with better outcomes.
- **Win rates** are typically **lower during Fear**, especially in high-leverage trades.
- Some accounts show signs of **overtrading** in Greed.
- Logistic regression model gives moderate accuracy in predicting profitable trades based on sentiment and trade attributes.


1. Clone the repo:
   ```bash
   git clone https://github.com/Tejabe/trader-behavior-insights.git
   cd trader-behavior-insights
