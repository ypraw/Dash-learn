import dash_html_components as html
import dash_core_components as dcc
from components.header import Header
# from app import app

content = html.Div(id="page-content")

layout = html.Div([dcc.Location(id="url"), html.Div([Header()]), content])
