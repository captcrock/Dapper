import pandas as pd
import numpy as np
from datetime import datetime

def clean_transaction_data(df):
    """
    Common data cleaning operations you might need to perform:
    - Handle missing values
    - Standardize formats
    - Remove duplicates
    - Fix data types
    """
    # Convert date strings to datetime
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
    
    # Standardize string columns
    df['customer_id'] = df['customer_id'].str.strip().str.upper()
    
    # Handle missing values
    df['amount'] = df['amount'].fillna(df['amount'].mean())
    
    # Remove duplicates
    df = df.drop_duplicates(subset=['transaction_id'])
    
    # Create derived columns
    df['transaction_month'] = df['transaction_date'].dt.to_period('M')
    
    return df

# Example usage
data = {
    'transaction_id': ['001', '002', '002', '003'],
    'customer_id': [' abc123 ', 'DEF456', 'GHI789', 'JKL012'],
    'amount': [100.0, None, 300.0, 400.0],
    'transaction_date': ['2024-01-01', '2024-01-02', '2024-01-02', 'invalid_date']
}
df = pd.DataFrame(data)
cleaned_df = clean_transaction_data(df)