def validate_dataset(df, rules):
    """
    Common validation scenarios:
    - Check data completeness
    - Validate business rules
    - Ensure data consistency
    """
    validation_results = {
        'total_records': len(df),
        'validations': {}
    }
    
    # Check for nulls in required fields
    null_checks = df.isnull().sum()
    validation_results['validations']['null_checks'] = null_checks.to_dict()
    
    # Validate numeric ranges
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if col in rules.get('range_checks', {}):
            min_val, max_val = rules['range_checks'][col]
            invalid_count = len(df[(df[col] < min_val) | (df[col] > max_val)])
            validation_results['validations'][f'{col}_range'] = invalid_count
    
    # Check unique constraints
    for col in rules.get('unique_columns', []):
        duplicate_count = len(df[df.duplicated(subset=[col], keep=False)])
        validation_results['validations'][f'{col}_uniqueness'] = duplicate_count
    
    return validation_results