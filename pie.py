import plotly.graph_objects as go # or plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd


df = pd.read_csv('play.csv')

opts = [{'label' : 'TEST', 'value' : 'TEST'}]

graphs={}
for i in df['PlaylistName'].unique():
    opts.append({'label' : i, 'value' : i})


def create_pie(df):
    fig = go.Figure(data=[go.Pie(
        labels=['total','found','inf'],
        values=[df['total'].sum(), df['captured'].sum(), df['pirate'].sum()]
        )])
    fig.update_traces(hole=.4, hoverinfo="value+label")
    fig.update_layout(
    annotations=[dict(text=str(df['total'].sum()), x=0.5, y=0.5, font_size=20, showarrow=False)])

    graphs['pie'] = fig

create_pie(df)
app = dash.Dash()
app.layout = html.Div([
                # adding a plot
                dcc.Graph(id ='pie', figure = graphs['pie']),
                # dropdown
                html.P([
                    html.Label("Choose a feature"),
                    dcc.Dropdown(id = 'opt',
                                 options = opts,
                                 value = 'TEST')
                        ], style = {'width': '400px',
                                    'fontSize' : '20px',
                                    'padding-left' : '100px',
                                    'display': 'inline-block'}),
                html.P([
                    html.Label(id='name', children='aaa'),
                    ]),
                      ])

# @app.callback(Output('pie', 'figure'),
#              [Input('opt', 'value')])

@app.callback(
    [Output('pie', 'figure'),Output('name', 'children'),],
    [Input('opt', 'value')]
    )
def update_pie(val):
    if val == 'TEST':
        create_pie(df)
    else:
        create_pie(df.loc[df['PlaylistName'] == val])
    return graphs['pie'], val


app.run_server(debug=True)
