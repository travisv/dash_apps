from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd

# create the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
           suppress_callback_exceptions=True)

# load out initial dataset
df = pd.read_csv('/home/travis/dash_apps/data/test_data.csv')
data_store = {'data': []}
