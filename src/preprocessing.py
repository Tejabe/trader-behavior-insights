import pandas as pd

def load_trader_data(path):
    df = pd.read_csv(path)

    if 'Timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')  # 👈 use the actual column
    else:
        raise ValueError("No valid time column found in trader data.")

    return df

def load_sentiment_data(path):
    df = pd.read_csv(path, parse_dates=['date'])
    return df

def clean_trader_data(df):
    df = df.dropna(subset=['timestamp'])

    # Standardize column names (remove spaces, lowercase, unify)
    df.columns = df.columns.str.strip().str.replace(" ", "").str.lower()

    return df

def clean_sentiment_data(df):
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date', 'value'])
    return df
    
