from dash.dependencies import Input, Output
from app import app
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import dash_html_components as html
from pages.bootstrap.bootstrap_model import query_dataframe


@app.callback(Output('graph-with-slider', 'figure'),
              Input('year-slider', 'value'))
def update_figure(selected_year):
    skripsi_data = query_dataframe()
    filtered_df = skripsi_data[skripsi_data['Tahun_Lulus'] == selected_year]
    filtered_df = filtered_df.groupby(
        'Kategori')["Kategori"].count().reset_index(name='Total')
    graph = {
        "data": [
            go.Bar(
                x=filtered_df['Kategori'],
                y=filtered_df['Total'],
                text=filtered_df['Total'],
                textposition='inside',
                textfont=dict(size=14,),
                marker={
                    "color": "#75E6DA",
                    "line": {
                        "color": "rgb(255, 255, 255)",
                        "width": 2,
                    },
                },
            ),
        ],
        "layout":
            go.Layout(
                autosize=True,
                bargap=0.35,
                font={
                    "family": "Raleway",
                },
                hovermode="closest",
                legend={
                    "x": -0.0228945952895,
                    "y": -0.189563896463,
                    "orientation": "h",
                    "yanchor": "top",
                },
                margin={
                    "r": 0,
                    "t": 20,
                    "b": 10,
                    "l": 10,
                },
                showlegend=True,
                xaxis={
    # "autorange": True,
                    "fixedrange": True,
                    "showline": True,
                    "title": "Gender",
                    "type": "category",
                    "automargin": True,
                },
                yaxis={
                    "showgrid": True,
                    "showline": True,
                    "title": "Grand Total",
                    "automargin": True,
                    "fixedrange": True,
                },
            ),
    }
    return graph


@app.callback(Output('table-data-skripsi', 'children'),
              Input('year-slider', 'value'))
def update_table(selected_year):
    skripsi_data = query_dataframe()
    filtered_df = skripsi_data[skripsi_data['Tahun_Lulus'] == selected_year]
    filtered_df.columns = ['Tahun Lulus', 'Judul', 'Kategori']
    top5 = filtered_df.sample(n=10)
    filtered_df = filtered_df.groupby(
        'Kategori')["Kategori"].count().reset_index(name='Total')
    summaryRes = [
        dbc.Card([
            dbc.CardHeader(html.H4("10 Data Sample"),
                           className="bg-info",
                           style={
                               "text-align": "center",
                               "color": "white"
                           }),
            dbc.CardBody([
                html.H5(className="card-title font-size-custom"),
                dbc.Row(
                    dbc.Col(dbc.Table.from_dataframe(top5,
                                                     striped=True,
                                                     bordered=True,
                                                     hover=True,
                                                     className="thead-dark"),
                            width={
                                "size": 10,
                                "offset": 1,
                            }),
                    align="center",
                ),
            ]),
        ],)
    ]

    return summaryRes