from typing import Iterable, Mapping
import pandas as pd
import re

from dash import Input, Output, State, html
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import yfinance as yf
from constants import fred

from app import app, df
from layouts import homepage, company_page, fred_page, industry_page, commodity_page

### Router ###
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    '''renders the correct page content based on the url path '''
    if pathname == "/":
        return [html.P("This is the content of the home page!"), homepage]
    elif pathname == "/company_overview":
        return company_page
    elif pathname == "/industries":
        return industry_page
    elif pathname == "/fred":
        return fred_page
    elif pathname == "/commodities":
        return commodity_page
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

### Price chart ###
@app.callback(Output('price-chart', 'figure'),
    Input('ticker-dropdown', 'value'))
def render_price_chart(ticker):
    '''Downloads price data from yfinance and displays in a chart price history.'''
    if ticker is None:
        raise PreventUpdate
    df = yf.download(ticker).reset_index()
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Adj Close']))
    fig.add_trace(go.Bar(x=df['Date'], y=df['Volume']), secondary_y=True)
    #fig = px.line(df, x='Date', y='Adj Close')
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(count=5, label="5y", step="year", stepmode="backward"),
                dict(count=10, label="10y", step="year", stepmode="backward"),
                dict(count=20, label="20y", step="year", stepmode="backward"),
                dict(step="all")
            ])
    ))
    return fig

### FRED chart ###
@app.callback(Output('fred-chart', 'figure'),
              Input('fred-dropdown', 'value'),
              Input('log-switch', 'on'))
def render_fred_chart(indicator, log_switch):
    '''Downloads data from FRED and displays in a chart.'''
    if indicator is None:
        raise PreventUpdate
    data = fred.get_series(indicator)
    data = pd.DataFrame(data, columns=['indicator']).dropna().reset_index()
    fig = px.area(data, x='index', y='indicator', log_y=log_switch)
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(count=5, label="5y", step="year", stepmode="backward"),
                dict(count=10, label="10y", step="year", stepmode="backward"),
                dict(count=25, label="25y", step="year", stepmode="backward"),
                dict(step="all")
            ])
    ))
    return fig

### Industry chart ###
@app.callback(Output('industry-chart', 'figure'),
              Input('industry-dropdown', 'value'))
def render_industry_chart(industry):
    '''Displays industry chart'''
    if industry is None:
        raise PreventUpdate
    dff = df[df['industry'] == industry]
    dff = dff.groupby('year').sum().reset_index()
    dff = dff.melt(id_vars=['year'], value_vars=[
        'revenue',
        'cogs',
        'operating_income'
    ])
    fig = px.bar(dff, x='year', y='value', facet_row='variable', height=800)

    # Sick way to rescale axis of a faceted figure -- found on stackoverflow
    for k in fig.layout:
        if re.search('yaxis[1-9]+', k):
            fig.layout[k].update(matches=None)
    return fig


### Commodity chart ###
@app.callback(Output('commodity-chart', 'figure'),
              Input('commodity-dropdown', 'value'))
def render_commodity_chart(commodity):
    '''Displays commodity chart'''
    if commodity is None:
        raise PreventUpdate
    df = yf.download(commodity).reset_index()
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Adj Close']))
    fig.add_trace(go.Bar(x=df['Date'], y=df['Volume']), secondary_y=True)
    #fig = px.line(df, x='Date', y='Adj Close')
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(count=5, label="5y", step="year", stepmode="backward"),
                dict(count=10, label="10y", step="year", stepmode="backward"),
                dict(count=20, label="20y", step="year", stepmode="backward"),
                dict(step="all")
            ])
    ))
    return fig


#######
# OLD
#######
"""
@app.callback(
    Output('my-ul', 'children'),
    [Input('my-button', 'n_clicks')],
    [State('my-input', 'value')],
)
def add_task(
    n_clicks: int = 0,
    value: str = None,
    data_store: Mapping[str, Iterable] = data_store,
) -> Iterable[html.Li]:
    '''Called when the button is clicked'''
    if value is not None and len(value.strip()):
        data_store['data'].append(value.strip())

    return list_tasks(data_store['data'])
"""
