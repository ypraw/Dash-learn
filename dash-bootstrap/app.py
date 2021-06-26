import dash
import dash_bootstrap_components as dbc

from flask_caching import Cache

# from utils.external_assets import FONT_AWSOME, CUSTOM_STYLE
from layout.layout import layout

import flask

server = flask.Flask(__name__)    # define flask app.server

FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
)

app = dash.Dash(
    __name__,
    server=server,
    suppress_callback_exceptions=True,
    meta_tags=[{
        'name': 'viewport',
        'content': 'width=device-width, initial-scale=1'
    }],
    external_stylesheets=[dbc.themes.MINTY, FONT_AWESOME],
)
app.title = "Dash Bootstrap"

cache = Cache(app.server,
              config={
                  'CACHE_TYPE': 'filesystem',
                  'CACHE_DIR': 'cache-directory',
                  'CACHE_THRESHOLD': 5,
              })

app.layout = layout

server = app.server