import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

# layout ={
#     paper_bgcolor='rgba(0,0,0,0)',
#     plot_bgcolor='rgba(0,0,0,0)'
# }

# MAP
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
map = go.Figure(data=go.Choropleth(
    locations = df['CODE'],
    z = df['GDP (BILLIONS)'],
    text = df['COUNTRY'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '$',
    colorbar_title = 'GDP<br>Billions US$',
))

map.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',

)
map.update_geos(
    visible=False,
    showcountries=True, countrycolor="#fb7813",
    showocean=True, oceancolor="#414141",
)

# PIE
df = px.data.tips()
pie = px.pie(df, values='tip', names='day', color='day',
             color_discrete_map={'Thur':'lightcyan',
                                 'Fri':'cyan',
                                 'Sat':'royalblue',
                                 'Sun':'darkblue'})

pie.update_layout(plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)',
    legend=dict(
        font=dict(
            family="sans-serif",
            size=18,
            color="#ca3e47"
        ),
    )
)

# line
import numpy as np

x = np.arange(10)

line = go.Figure(data=go.Scatter(x=x, y=x**2, mode='lines+markers', line_color='red'))
line.update_layout(
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=True,
        tickfont=dict(
            family='Arial',
            size=12,
            color='#b6eb7a',
        ),
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=True,
        tickfont=dict(
            family='Arial',
            size=12,
            color='#b6eb7a',
        ),
    ),
    autosize=False,
    showlegend=False,
    plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)'
)

app = dash.Dash()

app.layout = html.Div( className = 'main-container darkest-grey',
		children=[
			html.Div( # left dv
				className = 'main-left dark-grey',
                children =[
                    html.Div(
                        className = 'playlist-info',
                        children = [
                            html.Div(className= 'info'),
                            html.Div(className= 'pie',
                                children = dcc.Graph(figure=pie)
                            )

                        ]
                    )
                ]
			),
			html.Div( # right div
				className = 'main-right dark-grey',
				children=[
                    html.Div(className= 'graph',
                    children = dcc.Graph(figure=map)
                    ),
                    html.Div(className= 'graph',
                    children = dcc.Graph(figure=map)
                    ),
                    html.Div(className= 'graph',
                    children = dcc.Graph(figure=line)
                    ),
                      ]
			)
		]
	)


if __name__ == '__main__':
	app.run_server(debug = True)
