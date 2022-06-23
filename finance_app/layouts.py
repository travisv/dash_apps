from typing import Iterable, Mapping
import pandas as pd

import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc

from app import app, df
from styles import SIDEBAR_STYLE, CONTENT_STYLE, COMPANY_PAGE


"""
This app creates a simple sidebar layout using inline style arguments and the
dbc.Nav component.

dcc.Location is used to track the current location, and a callback uses the
current location to render the appropriate page content. The active prop of
each NavLink is set automatically according to the current pathname. To use
this feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""

############
# Components
#############

ticker_dropdown = dbc.Container([
    dbc.Label('Select ticker:'),
    dcc.Dropdown(id='ticker-dropdown',
                 value='^GSPC',
                 options=[{'label': ticker, 'value': ticker}
                          for ticker in df['symbol'].unique().tolist()],
                 style={'width':'250px'})
])


price_chart = dbc.Container([
    html.Br(),
    html.Br(),
    dbc.Label('Price chart:'),
    dcc.Graph(id='price-chart')
])

industry_dropdown = dbc.Container([
    dbc.Label('Select indicator:'),
    dcc.Dropdown(id='industry_page_indicator_dropdown',
                 placeholder='Choose an indicator',
                 value='revenue',
                 options=[{'label': indicator, 'value': indicator}
                          for indicator in ['Option 1', 'Option 2']]),
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
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

#########
# Pages
#########

content = html.Div(id="page-content", style=CONTENT_STYLE)

homepage = dbc.Container([
    html.H1('Home Page'),
])


company_page = dbc.Container([
    ticker_dropdown,
    price_chart
], style=COMPANY_PAGE)


def main_layout() -> html.Div:
    return html.Div(
        children=[
            dcc.Location(id='url'),
            sidebar,
            content
        ]
    )


#####
# OLD
#####
#main_layout = html.Div([
#    html.Div([
#        dbc.NavbarSimple([
#            # Dropdown to select the industry you want to look at
#            dbc.DropdownMenu([
#                dbc.DropdownMenuItem(industry, href=industry)
#                for industry in industries], label='Select industry'),],
#            brand='Home',brand_href='/', color='primary', dark=True,
#            className='font-weight-bold'),
#        dbc.Row([
#            dbc.Col(lg=1, md=1, sm=1),
#            dbc.Col([
#                # Get location to display correct content based on url
#                dcc.Location(id='location'),
#                html.Div(id='main_content')
#            ], lg=10),
#        ]),
#        html.Br(),
#    ], style={'backgroundColor': '#E5ECF6'})
#])
