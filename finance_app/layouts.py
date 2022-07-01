from typing import Iterable, Mapping
import pandas as pd

import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc

from app import app, df
from styles import SIDEBAR_STYLE, CONTENT_STYLE, COMPANY_PAGE

################
### Dropdowns
################
ticker_dropdown = dbc.Container([
    dbc.Label('Select ticker:'),
    dcc.Dropdown(id='ticker-dropdown',
                 value='^GSPC',
                 options=[{'label': ticker, 'value': ticker}
                          for ticker in df['symbol'].unique().tolist()],
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
                 options=[{'label': indicator, 'value': indicator}
                          for indicator in ['GDP', 'SP500']]),
])

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
                dbc.NavLink("Industry Analysis", href="/page-2", active="exact"),
                dbc.NavLink("FRED", href="fred", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
################
### Charts
################
price_chart = dbc.Container([
    html.Br(),
    dbc.Label('Price chart:'),
    dcc.Graph(id='price-chart')
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

##########
### Pages
##########
content = html.Div(id="page-content", style=CONTENT_STYLE)

homepage = dbc.Container([
    html.H1('Home Page'),
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
def main_layout() -> html.Div:
    return html.Div(
        children=[
            dcc.Location(id='url'),
            sidebar,
            content
        ]
    )

