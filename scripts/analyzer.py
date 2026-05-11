from textblob import TextBlob
import pandas as pd

class FinancialAnalyzer:
    @staticmethod
    def get_sentiment(text):
        """
        Task 2: NLP Sentiment Analysis.
        Returns a score from -1 (Negative) to 1 (Positive).
        """
        if pd.isna(text) or text == "":
            return 0.0
        # This calculates the 'vibe' of the headline
        return TextBlob(str(text)).sentiment.polarity
    
    def get_sentiment(text):
        if pd.isna(text) or text == "": return 0.0
        return TextBlob(str(text)).sentiment.polarity
    
    @staticmethod
    def calculate_technical_indicators(df):
        df['Date'] = pd.to_datetime(df['Date']).dt.tz_localize(None)
        df = df.sort_values('Date')
        df['Daily_Return'] = df['Close'].pct_change()
        df['SMA_7'] = df['Close'].rolling(window=7).mean()
        return df
    
    @staticmethod
    def run_correlation(news_df, stock_df):
        """"
        Task 4: Align news sentiment with stock returns by date.
        """
        # 1. Prepare News: Group by date and get average sentiment
        news_df['date'] = pd.to_datetime(news_df['date']).dt.date
        daily_sentiment = news_df.groupby('date')['sentiment_score'].mean().reset_index()
        daily_sentiment.columns = ['Date', 'Avg_Sentiment']

        # 2. Prepare Stock: Ensore Date is only the date (no time)
        stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.date

        # 3. Merge: Only keep dates where both news and stock data exist
        merged_df = pd.merge(daily_sentiment, stock_df, on='Date', how='inner')

        # 4. Correlation calculation
        correlation = merged_df['Avg_Sentiment'].corr(merged_df['Daily_Return'])
        return correlation, merged_df

    @staticmethod
    def categorize_sentiment(score):
        """
        Categorizes scores for the report visualizations.
        """
        if score > 0.1:
            return 'Positive'
        elif score < -0.1:
            return 'Negative'
        else:
            return 'Neutral'
        
    @staticmethod
    def calculate_technical_indicators(df):
        """Tak 3: Compute Daily Returns and SMAs."""
        # Ensure date is sorted
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values('Date')

        # 1. Daily Percentage Change
        df['Daily_Return'] = df['Close'].pct_change()

        # 2. 7-Day & 21-Day Moving Averages
        df['SMA_7'] = df['Close'].rolling(window=7).mean()
        df['SMA_21'] = df['Close'].rolling(window=21).mean()

        return df