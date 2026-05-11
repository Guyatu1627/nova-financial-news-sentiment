# Nova Financial News Sentiment Analysis
### Developed by Guyatu Gelgelo

## Project Overview
This project correlates financial news sentiment (1.4M articles) with stock market movements (AAPL) to help Nova Financial Solutions discover predictive signals.

## Project Structure
- `scripts/`: Python modules for data loading and analysis.
- `notebooks/`: Step-by-step exploration of EDA and Correlation.
- `tests/`: Automated unit tests for sentiment logic.
- `src/`: Streamlit dashboard code.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run Tests: `python -m unittest discover tests`
3. Launch Dashboard: `streamlit run src/app.py`