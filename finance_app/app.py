from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd
import sys
sys.path.append('/home/travis/dash_apps/data')
from clean_financial_data import get_data

# create the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
           suppress_callback_exceptions=True)

# load out initial dataset
df = get_data()
data_store = {'data': []}
