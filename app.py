import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from components import *
from functions import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA])

server = app.server

app.layout = dbc.Container(fluid=True,children=[
    html.Div(id='navbar',children=[navbar]),
    html.Img(id='banner',src='/assets/rooted-csa-header-2.jpg'),
    dbc.Row(class_name='pad-row'),
    dbc.Row(id='form',children=[dbc.Col(id='left-pad',width=1),dbc.Col(children=[html.H2('Growing Good Health'),form],width=6),dbc.Col()]),
    dbc.Row(children=[dbc.Col(width=1),dbc.Col(check_button,width=5)]),
    html.Div(id='display-value')
])


if __name__ == '__main__':
    app.run_server(debug=True)
