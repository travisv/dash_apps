from typing import Iterable, Mapping

from dash import dcc, html, dash_table

from app import app, data_store


def list_tasks(tasks: Iterable[str]) -> Iterable[html.Li]:
    '''Return list items of tasks.'''

    return [html.Li(children=tasks) for task in tasks]


def main_layout() -> html.Div:
    return html.Div(
        children=[
            html.H1('To Do List'),
            html.Ul(id='my-ul', children=list_tasks(data_store['data'])),
            dcc.Input(id='my-input'),
            html.Button(id='my-button', n_clicks=0, children='Add'),
        ]
    )
