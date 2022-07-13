from typing import Iterable, Mapping
import pandas as pd

import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc

from app import app, df
from styles import SIDEBAR_STYLE, CONTENT_STYLE, COMPANY_PAGE
from constants import COMMODITIES, FRED_INDICATORS

''' DROPDOWNS '''
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

''' CHARTS '''

price_chart = dbc.Container([
    html.Br(),
    dbc.Label('Price chart:'),
    dcc.Graph(id='price-chart')
])

commodity_chart = dbc.Container([
    html.Br(),
    dbc.Label('Commodity chart:'),
    dcc.Graph(id='commodity-chart')
])

fred_chart = dbc.Container([
    html.Br(),
    dbc.Label('FRED chart:'),
    dcc.Graph(id='fred-chart')
])

industry_chart = dbc.Container([
    html.Br(),
    dbc.Label('Industry chart:'),
    dcc.Graph(id='industry-chart')
])

''' PAGES '''
homepage = dbc.Container([
    html.H1('Home Page'),
])

commodity_page = dbc.Container([
    commodities_dropdown,
    commodity_chart
])

company_page = dbc.Container([
    ticker_dropdown,
    price_chart
], style=COMPANY_PAGE)

fred_page = dbc.Container([
    fred_dropdown,
    fred_chart
])

industry_page = dbc.Container([
    industry_dropdown,
    industry_chart
])

##############
# Main Layout
##############

sidebar = html.Div(
    [
        html.H2("Fiancial Analysis", className="display-6"),
        html.Hr(),
        html.P(
            "Select a page below", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Company Overview", href="/company_overview", active="exact"),
                dbc.NavLink("Industry Analysis", href="/industries", active="exact"),
                dbc.NavLink("FRED", href="/fred", active="exact"),
                dbc.NavLink("Commodities", href="/commodities", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

def main_layout() -> html.Div:
    return html.Div(
        children=[
            dcc.Location(id='url'),
            sidebar,
            content
        ]
    )

