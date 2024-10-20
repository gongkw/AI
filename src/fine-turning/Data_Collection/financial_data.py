import yfinance as yf

# Define the ticker symbol for Apple
ticker = "AAPL"

# Fetch the financial data
apple = yf.Ticker(ticker)

# Get quarterly financials
quarterly_financials = apple.quarterly_financials

# Get balance sheet data
quarterly_balance_sheet = apple.quarterly_balance_sheet

# Display the data
print("Quarterly Financials:")
print(quarterly_financials)

print("\nQuarterly Balance Sheet:")
print(quarterly_balance_sheet)

# Extract relevant information
net_income = quarterly_financials.loc['Net Income']
eps = quarterly_financials.loc['Diluted EPS']
revenue = quarterly_financials.loc['Total Revenue']
total_assets = quarterly_balance_sheet.loc['Total Assets']
liabilities = quarterly_balance_sheet.loc['Total Liabilities Net Minority Interest']

# Combine data into a DataFrame for better visualization
import pandas as pd

data = {
    'Net Income': net_income,
    'Earnings Per Share (EPS)': eps,
    'Revenue': revenue,
    'Total Assets': total_assets,
    'Total Liabilities': liabilities
}


financial_data = pd.DataFrame(data)

financial_data.to_csv('apple_financials_2013_2015.csv')