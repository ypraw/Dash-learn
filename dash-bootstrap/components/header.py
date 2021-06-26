import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


def Header():
    return html.Div([get_header(), html.Br([])])


def get_header():
    header = html.Div(
        [
            dbc.NavbarSimple(
                children=[
                    dbc.ButtonGroup(
    # Use row and col to control vertical alignment of logo / brand
                        [
                            dbc.Button(
                                "Dash Bootstrap",
                                href="/dashboard/dash-bootstrap-learn",
                                className="btn-link",
                                color="primary",
                                size="lg",
                                outline=True,
                                style={"color": "#fff"},
                            ),
                        ],),
                ],
                brand="Dash Bootstrap Learn",
                brand_style={
                    "font-size": "2.1rem",
                    "font-weight": "bold",
                },
                color="#05445E",
                dark=True,
                fluid=True,
            ),
        ],)

    return header
