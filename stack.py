import plotly.graph_objects as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go


animals=['giraffes', 'orangutans', 'monkeys']

fig = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=[0, 0, 3]),
    go.Bar(name='LA Zoo', x=animals, y=[0, 2, 0])
])
# Change the bar mode
fig.update_layout(barmode='stack',
        yaxis = go.YAxis(
        showticklabels=False),
        hovermode=False)

app = dash.Dash()
app.layout = html.Div(
    className='div',
    children=[
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)
