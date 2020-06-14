import plotly.graph_objects as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

df = pd.read_csv('maps.csv')
#
# fig = go.Figure(data=go.Choropleth(
#     locations = df['CODE'],
#     z = df['GDP (BILLIONS)'],
#     text = df['COUNTRY'],
#     colorscale = 'Blues',
#     autocolorscale=False,
#     reversescale=True,
#     marker_line_color='darkgray',
#     marker_line_width=0.5,
#     colorbar_tickprefix = '$',
#     colorbar_title = 'GDP<br>Billions US$'
# ))
#
# fig.update_layout(
#     geo=dict(
#         showframe=False,
#         showcoastlines=False,
#         projection_type='equirectangular'
#     ),
#     margin=dict(
#         l=10,
#         r=10,
#         b=10,
#         t=10,
#         pad=4
#     ),
#
# )
fig = px.choropleth(df, locations=df['CODE'], color=df['GDP (BILLIONS)'], animation_frame=df['YEAR'],
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(
    geo=dict(
        showframe=False,
        showcountries=True,
        projection_type='equirectangular'
    ),
    margin={"r":0,"t":0,"l":0,"b":0}
    )
fig["layout"].pop("updatemenus")


app = dash.Dash()
app.layout = html.Div(
    className='div',
    children=[
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)
