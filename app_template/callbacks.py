from typing import Iterable, Mapping

from dash import Input, Output, State, html
from app import app, data_store
from layouts import list_tasks



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
