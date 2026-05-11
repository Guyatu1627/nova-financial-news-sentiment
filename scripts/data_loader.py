import pandas as pd
import os

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Loads the raw CSV data from the data folder."""
        if not os.path.exists(self.file_path):
            print(f"❌ Error: File not found at {self.file_path}")
            return None
        self.df = pd.read_csv(self.file_path)
        print(f"✅ Loaded {len(self.df)} rows.")
        return self.df

    def clean_data(self):
        """Standardizes dates and removes nulls for Task 1."""
        if self.df is not None:
            # Convert date column to datetime objects
            self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
            # Remove rows where date or headline is missing
            self.df = self.df.dropna(subset=['date', 'headline'])
            # Remove indexing column if it exists
            if 'Unnamed: 0' in self.df.columns:
                self.df = self.df.drop(columns=['Unnamed: 0'])
            print("✅ Data cleaning complete.")
            return self.df