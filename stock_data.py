from api_keys import *
import alpaca_trade_api as tradeapi
import pandas as pd

spy_stocks_file = 'constituents_csv.csv'

spy_stocks = pd.read_csv(spy_stocks_file)
industrial = spy_stocks.loc[spy_stocks['Sector'] == 'Industrials']['Symbol'].values
health_care = spy_stocks.loc[spy_stocks['Sector'] == 'Health Care']['Symbol'].values
info_tech = spy_stocks.loc[spy_stocks['Sector'] == 'Information Technology']['Symbol'].values
com_services = spy_stocks.loc[spy_stocks['Sector'] == 'Communication Services']['Symbol'].values
consumer_staples = spy_stocks.loc[spy_stocks['Sector'] == 'Consumer Staples']['Symbol'].values
consumer_discretionary = spy_stocks.loc[spy_stocks['Sector'] == 'Consumer Discretionary']['Symbol'].values
utilities = spy_stocks.loc[spy_stocks['Sector'] == 'Utilities']['Symbol'].values
financials = spy_stocks.loc[spy_stocks['Sector'] == 'Financials']['Symbol'].values
materials = spy_stocks.loc[spy_stocks['Sector'] == 'Materials']['Symbol'].values
real_estate = spy_stocks.loc[spy_stocks['Sector'] == 'Real Estate']['Symbol'].values
energy = spy_stocks.loc[spy_stocks['Sector'] == 'Energy']['Symbol'].values


def data(sector):
    alpaca = tradeapi.REST(
        alpaca_api,
        alpaca_secret,
        api_version="v2")
    timeframe = "1D"
    start = pd.Timestamp("2017-07-13", tz="America/New_York").isoformat()
    end = pd.Timestamp("2021-07-01", tz="America/New_York").isoformat()
    df_tickers = alpaca.get_barset(
        sector,
        timeframe,
        start=start,
        end=end,
        limit=1000
    ).df
    return df_tickers


industrial_closes = pd.DataFrame()
health_care_closes = pd.DataFrame()
info_tech_closes = pd.DataFrame()
com_services_closes = pd.DataFrame()
consumer_staples_closes = pd.DataFrame()
consumer_discretionary_closes = pd.DataFrame()
utilities_closes = pd.DataFrame()
financials_closes = pd.DataFrame()
materials_closes = pd.DataFrame()
real_estate_closes = pd.DataFrame()
energy_closes = pd.DataFrame()


def closes(sector, dataframe):
    ohlc = data(sector)
    for stocks in sector:
        dataframe[stocks] = ohlc[stocks]['close']
