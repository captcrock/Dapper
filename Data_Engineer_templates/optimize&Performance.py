def optimize_data_processing(filepath, chunksize=10000):
    """
    Common optimization techniques:
    - Chunked processing
    - Vectorization
    - Efficient data structures
    """
    # Process large files in chunks
    chunks = []
    for chunk in pd.read_csv(filepath, chunksize=chunksize):
        # Vectorized operations instead of loops
        processed = chunk.assign(
            total = chunk['quantity'] * chunk['price'],
            discount = np.where(chunk['quantity'] > 10, 0.1, 0)
        )
        chunks.append(processed)
    
    # Efficient concatenation
    result = pd.concat(chunks, ignore_index=True)
    
    # Use appropriate data types
    result['category_id'] = result['category_id'].astype('category')
    
    return result