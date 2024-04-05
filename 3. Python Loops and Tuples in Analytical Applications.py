
'''
Task 1: Stock Market Data Analysis
Enhance your skills in data manipulation and analysis using tuples and loops.

Problem Statement:
You have been provided with stock market data, where each data point is a tuple containing a company's stock symbol, the date, 
and the closing price. Your task is to analyze this data to find the average closing price of a specified stock over a given period.

Sample Data:

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]
Create a function to calculate the average closing price of a specific stock symbol over all dates.
Ensure your solution handles cases where the stock symbol does not exist in the data.
'''

def calculate_average_closing_price(stock_data, stock_symbol):
    total_closing_price = 0
    count = 0
    
    for data_point in stock_data:
        symbol, _, closing_price = data_point
        if symbol == stock_symbol:
            total_closing_price += closing_price
            count += 1
    

    if count == 0:
        return f"No data found for stock symbol '{stock_symbol}'."
    else:
        average_closing_price = total_closing_price / count
        return f"Average closing price for {stock_symbol}: {average_closing_price}"

stock_data = [
    ("AAPL", "2021-01-01", 130.0), ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0), ("MSFT", "2021-01-02", 225.0),
    ("GOOGL", "2021-01-01", 1800.0), ("GOOGL", "2021-01-02", 1820.0)
]


print(calculate_average_closing_price(stock_data, "AAPL"))  # Average closing price for AAPL
print(calculate_average_closing_price(stock_data, "TSLA"))  # No data found for stock symbol 'TSLA'