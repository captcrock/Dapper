def analyze_sales_data(df):
    """
    Common aggregation operations:
    - Group by multiple dimensions
    - Calculate running totals
    - Compute period-over-period changes
    """
    # Monthly sales by category
    monthly_sales = df.groupby(['category', pd.Grouper(key='date', freq='M')])['amount'].sum()
    
    # Running total by customer
    df['running_total'] = df.groupby('customer_id')['amount'].cumsum()
    
    # Year-over-year growth
    yearly_sales = df.groupby([df['date'].dt.year, 'category'])['amount'].sum()
    yoy_growth = yearly_sales.pct_change()
    
    # Calculate customer metrics
    customer_metrics = df.groupby('customer_id').agg({
        'amount': ['count', 'sum', 'mean'],
        'date': lambda x: (x.max() - x.min()).days
    })
    
    return monthly_sales, yoy_growth, customer_metrics