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
    b = 0
    c = 0
    d = 0
    while x < len(test.beta):
        if test.beta.iloc[x] < 1 < test.sharpe_ratio.iloc[x] and test.annualized_std.iloc[x] < 0.5\
                and test.annualized_avg.iloc[x] > 0.05 and b < 5:
            conservative_portfolio.append(sectors[a][x])
            b += 1

        if test.beta.iloc[x] < 1.25 and test.sharpe_ratio.iloc[x] > 0.75 > test.annualized_std.iloc[x] and\
                test.annualized_avg.iloc[x] > 0.1 and c < 5:
            moderate_portfolio.append(sectors[a][x])
            c += 1

        if test.annualized_avg.iloc[x] > 0.2 and test.beta.iloc[x] > 1.25 and test.sharpe_ratio.iloc[x] > 0.5 and d < 5:
            aggressive_portfolio.append(sectors[a][x])
            d += 1
        x += 1
    a += 1

cons_calc = calc(conservative_portfolio)
mod_calc = calc(moderate_portfolio)
agg_calc = calc(aggressive_portfolio)

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

cons_sim = conservative_ten_yr_sim.summarize_cumulative_return()
mod_sim = moderate_ten_yr_sim.summarize_cumulative_return()
agg_sim = aggressive_ten_yr_sim.summarize_cumulative_return()


print(f"""Conservative Portfolio: {conservative_portfolio}
          Beta: {round(cons_calc.beta.mean(), 2)}
          Sharpe Ratio: {round(cons_calc.sharpe_ratio.mean(), 2)}
          Annualized Average: {round(cons_calc.annualized_avg.mean(), 2) * 100}
          Simulated 10yr Cumulative Returns {round(cons_sim['mean'], 2)}%""")
print(f"""Moderate Portfolio: {moderate_portfolio}
          Beta: {round(mod_calc.beta.mean(), 2)}
          Sharpe Ratio: {round(mod_calc.sharpe_ratio.mean(), 2)}
          Annualized Average: {round(mod_calc.annualized_avg.mean(), 2) * 100}%
          Simulated 10yr Cumulative Returns {round(mod_sim['mean'], 2)}%""")
print(f"""Aggressive Portfolio: {aggressive_portfolio}
          Beta: {round(agg_calc.beta.mean(), 2)}
          Sharpe Ratio: {round(agg_calc.sharpe_ratio.mean(), 2)}
          Annualized Average: {round(agg_calc.annualized_avg.mean(), 2) * 100}%
          Simulated 10yr Cumulative Returns {round(agg_sim['mean'], 2)}%""")

# print(conservative_ten_yr_sim.summarize_cumulative_return()['mean'])
# print(moderate_ten_yr_sim.summarize_cumulative_return())
# print(aggressive_ten_yr_sim.summarize_cumulative_return())
