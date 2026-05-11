import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Add the project root to sys.path so we can import our scripts
base_path = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_path, '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from scripts.data_loader import DataLoader
from scripts.analyzer import FinancialAnalyzer

st.set_page_config(page_title="Nova Financial Analytics", layout="wide")

# --- DATA LOADING WITH ERROR HANDLING ---
@st.cache_data
def load_all_data():
    # Define paths relative to this script
    news_path = os.path.join(project_root, 'data', 'raw_analyst_ratings.csv')
    stock_path = os.path.join(project_root, 'data', 'AAPL.csv')

    # 1. Load News
    if not os.path.exists(news_path):
        st.error(f"❌ News file not found at: {news_path}. Ensure it is uploaded to GitHub.")
        st.stop()
        
    loader = DataLoader(news_path)
    news = loader.load_data()
    if news is None:
        st.error("❌ Failed to load News DataFrame.")
        st.stop()
        
    news = loader.clean_data()
    # Sample for performance on Cloud
    sample_news = news.head(10000).copy() 
    sample_news['sentiment_score'] = sample_news['headline'].apply(FinancialAnalyzer.get_sentiment)
    
    # 2. Load Stocks
    if not os.path.exists(stock_path):
        st.error(f"❌ Stock file not found at: {stock_path}")
        st.stop()
        
    stocks = pd.read_csv(stock_path)
    stocks = FinancialAnalyzer.calculate_technical_indicators(stocks)
    
    return sample_news, stocks

# Execution
news_df, stock_df = load_all_data()

# --- UI LAYOUT ---
st.title("📊 Nova Financial: News & Stock Intelligence")
st.markdown(f"**Analyst:** Guyatu Gelgelo | **Project:** Sentiment-Price Correlation")

tab1, tab2, tab3, tab4 = st.tabs(["Task 1: EDA", "Task 2: Sentiment", "Task 3: Quantitative", "Task 4: Correlation"])

with tab1:
    st.header("Exploratory Data Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Publication Trends")
        news_df['day'] = pd.to_datetime(news_df['date']).dt.day_name()
        fig, ax = plt.subplots()
        sns.countplot(data=news_df, x='day', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], palette='viridis', ax=ax)
        st.pyplot(fig)
    with col2:
        st.subheader("Headline Lengths")
        fig, ax = plt.subplots()
        sns.histplot(news_df['headline'].str.len(), bins=30, kde=True, color='teal', ax=ax)
        st.pyplot(fig)

with tab2:
    st.header("Sentiment Analysis")
    def label_sentiment(score):
        if score > 0.05: return 'Positive'
        elif score < -0.05: return 'Negative'
        return 'Neutral'
    news_df['sentiment_type'] = news_df['sentiment_score'].apply(label_sentiment)
    fig, ax = plt.subplots()
    news_df['sentiment_type'].value_counts().plot.pie(autopct='%1.1f%%', colors=['grey', 'green', 'red'], ax=ax)
    st.pyplot(fig)

with tab3:
    st.header("Technical Indicators")
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(stock_df['Date'], stock_df['Close'], label='Price', alpha=0.5)
    ax.plot(stock_df['Date'], stock_df['SMA_7'], label='7-Day SMA', color='orange')
    ax.plot(stock_df['Date'], stock_df['SMA_21'], label='21-Day SMA', color='red')
    ax.legend()
    st.pyplot(fig)

with tab4:
    st.header("Correlation Result")
    corr_val, merged_data = FinancialAnalyzer.run_correlation(news_df, stock_df)
    st.metric("Pearson Correlation", f"{corr_val:.4f}")
    fig, ax = plt.subplots()
    sns.regplot(x='Avg_Sentiment', y='Daily_Return', data=merged_data, ax=ax, line_kws={'color':'red'})
    st.pyplot(fig)