import pandas as pd

# Load dataset
df = pd.read_csv('sales.csv')

# Total sales by product
print(df.groupby('Product')['Revenue'].sum())

# Filter top-selling product
top_product = df.groupby('Product')['Revenue'].sum().idxmax()
print("Top-selling product:", top_product)










