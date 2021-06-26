import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from pages.bootstrap import bootstrap_layout


@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/dashboard/dash-bootstrap-learn':
        return bootstrap_layout.layout

    else:
        return bootstrap_layout.layout
