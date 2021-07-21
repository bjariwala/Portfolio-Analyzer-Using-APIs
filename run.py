from calculations import Calculations as calc
from stock_data import *

test = calc(utilities, utilities_closes)
print(test.sharpe_ratio.mean())
x = 0
while x < len(test.beta):
    if test.beta.iloc[x] < 1 < test.sharpe_ratio.iloc[x]:
        print(materials[x])
    x += 1
