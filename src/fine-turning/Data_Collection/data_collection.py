import yfinance as yf
#data = yf.download("AAPL", start="2015-01-01", end="2016-01-01")
data = yf.download("AAPL", start="2016-01-01", end="2017-01-01")



data['Daily_Volume_transaction'] = data['Volume'].pct_change()
data['Daily_Return'] = data['Adj Close'].pct_change()
data['Volatility'] = data['Daily_Return'].rolling(window=30).std() * (252**0.5)  # Annualized Volatility



#data.to_csv('AAPL_data.csv')
data.to_csv('Evaluation_AAPL_data.csv')
