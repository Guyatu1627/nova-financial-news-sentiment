import unittest
import sys
import os

# Add scripts to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.analyzer import FinancialAnalyzer

class TestFinancialAnalyzer(unittest.TestCase):
    def test_sentiment_positive(self):
        # Using very strong positive words
        text = "Apple stocks are excellent and successful with great growth"
        score = FinancialAnalyzer.get_sentiment(text)
        print(f"\nPositive Test Score: {score}")
        self.assertGreater(score, 0, f"Expected positive score, got {score}")

    def test_sentiment_negative(self):
        # Using very strong negative words
        text = "Apple stocks are terrible, awful, and failing miserably"
        score = FinancialAnalyzer.get_sentiment(text)
        print(f"Negative Test Score: {score}")
        self.assertLess(score, 0, f"Expected negative score, got {score}")

if __name__ == '__main__':
    unittest.main()