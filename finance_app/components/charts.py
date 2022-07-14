from dash import dcc, html
import dash_bootstrap_components as dbc


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
