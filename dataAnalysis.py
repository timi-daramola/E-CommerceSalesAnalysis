import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('ecommerce_sales.csv')

# Display the first few rows of the data
data.head()


# Remove rows with missing values
data = data.dropna()

# Convert 'InvoiceDate' to datetime
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# Ensure the 'UnitPrice' and 'Quantity' columns are numerical
data['UnitPrice'] = pd.to_numeric(data['UnitPrice'], errors='coerce')
data['Quantity'] = pd.to_numeric(data['Quantity'], errors='coerce')

# Create a 'TotalPrice' column to calculate the total sale per item
data['TotalPrice'] = data['UnitPrice'] * data['Quantity']


# Group data by 'Description' (product name) and sum the total sales
top_products = data.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(5)

# Display the top 5 products
print(top_products)


# Group data by 'Country' and calculate average total sale per transaction
avg_order_value = data.groupby('Country')['TotalPrice'].mean().sort_values(ascending=False)

# Display the average order value by country
print(avg_order_value)


# Extract year and month from 'InvoiceDate'
data['YearMonth'] = data['InvoiceDate'].dt.to_period('M')

# Group by 'YearMonth' and sum 'TotalPrice' for each month
monthly_sales = data.groupby('YearMonth')['TotalPrice'].sum()

# Plot the monthly sales trend
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
