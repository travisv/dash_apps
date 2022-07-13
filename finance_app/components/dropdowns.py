from typing import Iterable, Mapping
import pandas as pd

import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
from app import df

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
