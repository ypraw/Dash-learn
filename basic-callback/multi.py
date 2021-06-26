from math import pow, sqrt
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(
        id='x',
        type='number',
        value=3,

    ),
    dcc.Input(
        id='y',
        type='number',
        value=4
    ),
    html.Table([
        html.Tr([html.Td(['a', html.Sup(2)]), html.Td(id='a-square')]),
        html.Tr([html.Td(['b', html.Sup(3)]), html.Td(id='b-square')]),
        html.Tr([html.Td(['(a+b)',html.Sup(2)] ), html.Td(id='ab-sqsum')]),
        html.Tr([html.Td(['c']), html.Td(id='ab-sqr')]),

    ]),
])


@app.callback(
    Output('a-square', 'children'),
    Output('b-square', 'children'),
    Output('ab-sqsum', 'children'),
    Output('ab-sqr', 'children'),
    Input('x', 'value'),
    Input('y', 'value'))
def callback_pytagoras(x,y):
    a_square = pow(x,2)
    b_square = pow(y,2)
    aplusb =  a_square + b_square

    c = sqrt(aplusb)

    return a_square, b_square, aplusb, c


if __name__ == '__main__':
    app.run_server(debug=True)