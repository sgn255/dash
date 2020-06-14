import plotly.graph_objects as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]
tt = [str(i) for i in range(50)]

def names():
    return '<br>'.join([', '.join([v for v in tt[i: i+4]]) for i in range(0, len(tt), 4)])
# Use the hovertext kw argument for hover text
fig = go.Figure(data=[go.Bar(x=x, y=y,
            hovertext=[names(), '24% market share', '19% market share'])])
# Customize aspect
fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
fig.update_layout(title_text='January 2013 Sales Report')


app = dash.Dash()
app.layout = html.Div(
    className='div',
    children=[
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)
