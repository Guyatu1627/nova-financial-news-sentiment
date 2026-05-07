# Nova Financial News Sentiment Analysis

**KAIM Week 1 Challenge | 10 Academy**

## Project Overview

Predicting stock price movements using financial news sentiment analysis.
We analyze 1.4 million financial news headlines and correlate sentiment
scores with daily stock returns for AAPL, AMZN, GOOG, META, and NVDA.

## Business Question

> Can the sentiment of financial news headlines predict whether a stock
> price will go up or down the next trading day?

## Project Structure

```
nova-financial-news-sentiment/
├── data/raw/          <- Raw CSV data files (not tracked by Git)
├── notebooks/         <- Jupyter notebooks for each task
├── src/               <- Reusable Python source code
├── tests/             <- Unit tests
├── scripts/           <- Utility scripts
└── requirements.txt   <- Python dependencies
```

## Tasks

| Task | Description | Status |
|------|-------------|--------|
| Task 1 | Exploratory Data Analysis (EDA) | ✅ Complete |
| Task 2 | Technical Indicators (TA-Lib, PyNance) | 🔄 In Progress |
| Task 3 | Sentiment-Price Correlation Analysis | ⏳ Pending |

## Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/Guyatu1627/nova-financial-news-sentiment.git
cd nova-financial-news-sentiment

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch Jupyter
jupyter notebook
```

## Dataset

- **News Data:** 1.4M financial headlines (2011–2020) from Benzinga
- **Stock Data:** Daily OHLCV prices for AAPL, AMZN, GOOG, META, NVDA

## Author

Your Name | 10 Academy KAIM Cohort 9
