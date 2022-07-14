from typing import Iterable, Mapping
import pandas as pd

import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import dash_daq as daq

from app import app, df
from styles import SIDEBAR_STYLE, CONTENT_STYLE, COMPANY_PAGE

from components.dropdowns import ticker_dropdown, commodities_dropdown, industry_dropdown, fred_dropdown
from components.charts import commodity_chart, price_chart, fred_chart, industry_chart

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
    daq.BooleanSwitch(id='log-switch', on=False, label='log-Y', labelPosition='top', color='#9B51E0'),
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

