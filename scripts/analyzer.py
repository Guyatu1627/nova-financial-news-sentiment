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