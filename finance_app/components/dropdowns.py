from typing import Iterable, Mapping
import pandas as pd

import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
from app import df
from constants import COMMODITIES, FRED_INDICATORS

''' DROPDOWNS used as input components'''
commodities_dropdown = dbc.Container([
    dbc.Label('Select commoidity:'),
    dcc.Dropdown(id='commodity-dropdown',
                 value='^GSPC',
                 options=[{'label': k, 'value': v}
                          for k,v in  COMMODITIES.items()],
                 style={'width':'250px'})
])

industry_dropdown = dbc.Container([
    dbc.Label('Select industry:'),
    dcc.Dropdown(id='industry-dropdown',
                 value='Banks',
                 options=[{'label': industry, 'value': industry}
                          for industry in df['industry'].dropna().unique()]),
])

fred_dropdown = dbc.Container([
    dbc.Label('Select indicator:'),
    dcc.Dropdown(id='fred-dropdown',
                 placeholder='Choose an indicator',
                 value='GDP',
                 options=[{'label': k, 'value': v}
                          for k,v in FRED_INDICATORS.items()]),
])

ticker_dropdown = dbc.Container([
    dbc.Label('Select ticker:'),
    dcc.Dropdown(id='ticker-dropdown',

                 value='AAPL',
                 # Add in yfinance commodity tickers, need to make their own
                 # page, not done yet
                 #options=[{'label': k, 'value': v}
                          #for k,v in  COMMODITIES.items()],
                 # Commentted out for quick test of yfinance commodites
                 options=[{'label': ticker, 'value': ticker}
                          for ticker in df['symbol'].unique().tolist()],
                 style={'width':'250px'})
])

