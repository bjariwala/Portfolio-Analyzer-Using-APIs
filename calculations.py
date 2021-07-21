import numpy as np
from stock_data import *


class Calculations:
    def __init__(self, sector):
        self.daily_returns = closes(sector).pct_change()
        self.cumulative_returns = self.daily_returns.cumsum()
        self.std_dev = self.daily_returns.std()
        self.annualized_std = (self.std_dev * np.sqrt(252))
        self.annualized_avg = (self.daily_returns.mean() * 252)
        self.sharpe_ratio = (self.annualized_avg / self.annualized_std)
        self.covar = (self.daily_returns.rolling(60).cov(data('SPY')['SPY']['close'].pct_change()))
        self.covar['SPY_Var'] = data('SPY')['SPY']['close'].pct_change().rolling(60).var()
        self.beta = self.covar.iloc[:, :].div(self.covar['SPY_Var'], axis=0).mean().drop('SPY_Var')
        self.sector_avg_beta = self.beta.mean()

