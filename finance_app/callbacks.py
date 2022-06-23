from typing import Iterable, Mapping

from dash import Input, Output, State, html
from dash.exceptions import PreventUpdate
from app import app, df
from layouts import homepage, company_page

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import dash_bootstrap_components as dbc

import yfinance as yf

### Router ###
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    '''renders the correct page content based on the url path '''
    if pathname == "/":
        return [html.P("This is the content of the home page!"), homepage]
    elif pathname == "/company_overview":
        return company_page
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


### Price chart ###
@app.callback(
    Output('price-chart', 'figure'),
    Input('ticker-dropdown', 'value')
)
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
