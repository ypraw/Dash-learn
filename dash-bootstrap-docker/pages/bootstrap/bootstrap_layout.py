import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.H4 import H4
from app import app
from pages.bootstrap.bootstrap_model import query_dataframe
import dash_bootstrap_components as dbc

layout = html.Div([
    # Start Container
    dbc.Container(
        [
    #
    # html.Div(html.Nav(html.H4("hello"))),
            html.Div([    # start Row
                dbc.Row(
                    dbc.Col(
                        html.Div(
                            [
                                dbc.Card([
                                    dbc.CardHeader(
                                        html.H4("Simple Graph with Bootstrap"),
                                        className="bg-info",
                                        style={
                                            "text-align": "center",
                                            "color": "white"
                                        }),
                                    dbc.CardBody([
                                        dcc.Graph(
                                            id='graph-with-slider',
                                            config={"displayModeBar": False},
                                        ),
                                    ]),
                                    dbc.CardFooter(
                                        dcc.Slider(
                                            id='year-slider',
                                            min=query_dataframe()
                                            ['Tahun_Lulus'].min(),
                                            max=query_dataframe()
                                            ['Tahun_Lulus'].max(),
                                            value=query_dataframe()
                                            ['Tahun_Lulus'].min(),
                                            marks={
                                                str(year): str(year)
                                                for year in query_dataframe()
                                                ['Tahun_Lulus'].unique()
                                            },
                                            step=None),)
                                ]),
                            ],
                            style={
                                "margin-bottom": "35px",
                            },
                        ),
    # className="col align-self-center",
                        width={
                            "size": 6,
                            "offset": 3
                        },
                    ),
    # End Row
                ),
    # Start Tag Div
                html.Div(
                    [
    # Start Row
                        dbc.Row([
                            dbc.Col([
                                dbc.Spinner(
                                    children=html.Div(id='table-data-skripsi'),
                                    color="success",
                                    size="lg",
                                ),
                            ],
                                    md=12,
                                    lg=12,
                                    xl=12,
                                    sm=12,
                                    xs=12,
                                    className="col"),
                        ],
                                justify="between"),
    # End Row
                    ],
                    style={
                        "margin-bottom": "35px",
                    },
                ),
    # End Tag Div
            ]),
        ],
    # Start Container
        fluid=True,
    ),
])