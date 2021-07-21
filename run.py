from calculations import Calculations as calc
from stock_data import *
from MCForecastTools import MCSimulation

sectors = [industrial, health_care, info_tech, com_services, consumer_staples, consumer_discretionary, utilities,
           financials, materials, real_estate, energy]

conservative_portfolio = []
moderate_portfolio = []
aggressive_portfolio = []
a = 0
while a < len(sectors):
    test = calc(sectors[a])
    x = 0
    while x < len(test.beta):
        if test.beta.iloc[x] < 1 < test.sharpe_ratio.iloc[x]:
            conservative_portfolio.append(sectors[a][x])

        if test.beta.iloc[x] < 1.25 and test.sharpe_ratio.iloc[x] > 0.75:
            moderate_portfolio.append(sectors[a][x])

        if test.annualized_avg.iloc[x] > 0.2 and test.beta.iloc[x] > 1.25:
            aggressive_portfolio.append(sectors[a][x])
        x += 1
    a += 1

print(f"Conservative Portfolio: {conservative_portfolio}")
print(f"Moderate Portfolio: {moderate_portfolio}")
print(f"Aggressive Portfolio: {aggressive_portfolio}")

conservative_portfolio_data = data(conservative_portfolio)
moderate_portfolio_data = data(moderate_portfolio)
aggressive_portfolio_data = data(aggressive_portfolio)

conservative_ten_yr_sim = MCSimulation(
    portfolio_data=conservative_portfolio_data,
    num_simulation=50,
    num_trading_days=252*10
)
moderate_ten_yr_sim = MCSimulation(
    portfolio_data=moderate_portfolio_data,
    num_simulation=50,
    num_trading_days=252*10
)
aggressive_ten_yr_sim = MCSimulation(
    portfolio_data=aggressive_portfolio_data,
    num_simulation=50,
    num_trading_days=252*10
)

print(conservative_ten_yr_sim.summarize_cumulative_return())
print(moderate_ten_yr_sim.summarize_cumulative_return())
print(aggressive_ten_yr_sim.summarize_cumulative_return())
