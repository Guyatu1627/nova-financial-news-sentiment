import pandas as pd
import os

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Loads the raw CSV data."""
        if not os.path.exists(self.file_path):
            print(f"❌ Error: File not found at {self.file_path}")
            return None
        self.df = pd.read_csv(self.file_path)
        print(f"✅ Loaded {len(self.df)} rows.")
        return self.df

    def clean_data(self):
        """Standardizes dates and removes missing values."""
        if self.df is not None:
            # 1. Convert date to datetime
            self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
            
            # 2. Drop rows with invalid dates or missing headlines
            self.df = self.df.dropna(subset=['date', 'headline'])
            
            # 3. Drop unwanted columns
            if 'Unnamed: 0' in self.df.columns:
                self.df = self.df.drop(columns=['Unnamed: 0'])
            
            print("✅ Data cleaned and self.df updated.")
            return self.df

    def get_task_1_stats(self):
        """Calculates EDA statistics for the report."""
        if self.df is None:
            raise ValueError("No data found. Did you run load_data() and clean_data()?")
        
        stats = {
            "headline_lengths": self.df['headline'].str.len(),
            "articles_per_publisher": self.df['publisher'].value_counts(),
            "publication_days": self.df['date'].dt.day_name().value_counts()
        }
        return stats