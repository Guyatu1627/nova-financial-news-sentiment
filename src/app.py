import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Add scripts to path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.data_loader import DataLoader
from scripts.analyzer import FinancialAnalyzer

st.set_page_config(page_title="Nova Financial Analytics", layout="wide")

# --- DATA LOADING ---
@st.cache_data # This makes the app fast by saving data in memory
def load_all_data():
    # Load News
    loader = DataLoader('data/raw_analyst_ratings.csv')
    news = loader.load_data()
    news = loader.clean_data()
    # Add sentiment scores (Calculating for a sample to keep it fast)
    sample_news = news.head(5000).copy()
    sample_news['sentiment_score'] = sample_news['headline'].apply(FinancialAnalyzer.get_sentiment)
    
    # Load Stocks
    stocks = pd.read_csv('data/AAPL.csv')
    stocks = FinancialAnalyzer.calculate_technical_indicators(stocks)
    
    return sample_news, stocks

news_df, stock_df = load_all_data()

# --- DASHBOARD HEADER ---
st.title("📊 Nova Financial: News & Stock Intelligence")
st.markdown(f"**Analyst:** Guyatu Gelgelo | **Project:** Sentiment-Price Correlation")

# Create Tabs for each Task
tab1, tab2, tab3, tab4 = st.tabs(["Task 1: EDA", "Task 2: Sentiment", "Task 3: Quantitative", "Task 4: Correlation"])

# --- TAB 1: EDA ---
with tab1:
    st.header("Exploratory Data Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Publication Frequency by Day")
        news_df['day'] = pd.to_datetime(news_df['date']).dt.day_name()
        fig, ax = plt.subplots()
        sns.countplot(data=news_df, x='day', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], ax=ax, palette='viridis')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with col2:
        st.subheader("Headline Length Distribution")
        news_df['len'] = news_df['headline'].str.len()
        fig, ax = plt.subplots()
        sns.histplot(news_df['len'], bins=30, kde=True, ax=ax, color='teal')
        st.pyplot(fig)

# --- TAB 2: SENTIMENT ---
with tab2:
    st.header("Sentiment Analysis Results")
    # Define categories
    def label_sentiment(score):
        if score > 0.05: return 'Positive'
        elif score < -0.05: return 'Negative'
        else: return 'Neutral'
    
    news_df['sentiment_type'] = news_df['sentiment_score'].apply(label_sentiment)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write(news_df['sentiment_type'].value_counts())
    with col2:
        fig, ax = plt.subplots()
        news_df['sentiment_type'].value_counts().plot.pie(autopct='%1.1f%%', colors=['grey', 'green', 'red'], ax=ax)
        st.pyplot(fig)

# --- TAB 3: QUANTITATIVE ---
with tab3:
    st.header("Stock Price & Technical Indicators")
    st.subheader("AAPL Price with 7-Day & 21-Day Moving Averages")
    
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(stock_df['Date'], stock_df['Close'], label='Close Price', alpha=0.5)
    ax.plot(stock_df['Date'], stock_df['SMA_7'], label='7-Day SMA', color='orange')
    ax.plot(stock_df['Date'], stock_df['SMA_21'], label='21-Day SMA', color='red')
    ax.legend()
    st.pyplot(fig)

# --- TAB 4: CORRELATION ---
with tab4:
    st.header("The Master Correlation")
    corr_val, merged_data = FinancialAnalyzer.run_correlation(news_df, stock_df)
    
    st.metric("Pearson Correlation Coefficient", f"{corr_val:.4f}")
    
    fig, ax = plt.subplots()
    sns.regplot(x='Avg_Sentiment', y='Daily_Return', data=merged_data, ax=ax, scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
    plt.title("Sentiment vs. Daily Returns")
    st.pyplot(fig)