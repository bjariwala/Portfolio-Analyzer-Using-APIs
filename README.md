Project Proposal

Clients will be able to use this application to analyze different portfolios based on varies factors including portfolio weights between stocks in the S&P 500, bonds, and the top cryptocurrencies offered on Coinbase, the Sharpe ratios, and overall portfolio returns. There will be three different portfolio risk tolerances: conservative, moderate, and aggressive. The application will be accessing APIs from Alpaca and Coinbase to source the data. Portfolio simulations will be generated using the Monte Carlo Simulations to project the potential returns.

Python Tools
- Anaconda: Pandas is included in Anaconda distribution and Conda package manager to manage Python environments.
- Jupyter Lab: web-based user interface designed for data analysis. It lets you write, run, and review the results in Python programs (all in a single integrated development environment (IDE).

Imported Libraries
- Pandas: clean/organize the data and to calculations
- Numpy: more calculations
- JSON: API into a human-readable format
- Requests: makes the API calls
- OS: interacting with the computer's operating system/grab the API keys from environment variables 
- donenv: load environment variables ex. API keys
- MCForecastTools: Monte Carlo Simulations to project potential returns

APIs for Data
- Alpaca: historical data for stocks and bonds.
- Coinbase: historical data for cryptocurrencies.
