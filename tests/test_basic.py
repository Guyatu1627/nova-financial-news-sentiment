# tests/test_basic.py
# Basic sanity tests for Task 1
# Run with: pytest tests/ -v

def test_python_version():
    """Make sure we are using Python 3.7+"""
    import sys
    assert sys.version_info >= (3, 7), "Python 3.7+ required"

def test_imports():
    """Make sure all required libraries are installed"""
    import pandas as pd
    import numpy as np
    import matplotlib
    import seaborn
    import sklearn
    assert True, "All imports successful"

def test_pandas_dataframe():
    """Basic pandas DataFrame creation test"""
    import pandas as pd
    df = pd.DataFrame({'headline': ['Test headline'], 'stock': ['AAPL']})
    assert len(df) == 1
    assert 'headline' in df.columns
    assert 'stock' in df.columns
