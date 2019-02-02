
#Resources: Basic Tutorials
#https://medium.freecodecamp.org/this-quick-intro-to-dash-will-get-you-to-hello-world-in-under-5-minutes-86f8ae22ca27
#https://www.datacamp.com/community/tutorials/learn-build-dash-python
#https://towardsdatascience.com/how-to-create-your-first-web-app-using-python-plotly-dash-and-google-sheets-api-7a2fe3f5d256


import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import os

import plotly.graph_objs as go
import plotly 
import plotly.plotly as py
import plotly.figure_factory as ff

df_sample = pd.read_csv('heat_map.csv')
df_sample_r = df_sample[df_sample['STNAME'] == 'California']

values = df_sample_r['RESULT'].tolist()
fips = df_sample_r['FIPS'].tolist()

endpts = list(np.mgrid[min(values):max(values):4j])
colorscale = [
    'rgb(193, 193, 193)',
    'rgb(239,239,239)',
    'rgb(195, 196, 222)',
    'rgb(144,148,194)',
    'rgb(101,104,168)',
    'rgb(65, 53, 132)'
]







#header_names =[ 'SchoolName', 'SchoolCounty', 'RESULT',]
df = pd.read_csv('./filtered.csv', header=0)
#filter the data frame here ... 
df= df[df.RESULT>5]

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = ['https://cdnjs.cloudflare.com/ajax/libs/foundation/6.5.3/css/foundation-float.css']

#app = dash.Dash()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#External CSS
""" external_css = ["https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
                "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css", ]
for css in external_css:
    app.css.append_css({"external_url": css}) """

#External JS
external_js = ["http://code.jquery.com/jquery-3.3.1.min.js",
               "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"]
for js in external_js:
    app.scripts.append_script({"external_url": js})

selected = ["ID", "WaterSystemCounty", "SchoolName", "RESULT"]
        

app.layout = html.Div(
    children =
        [html.H1(children='water visualization',
                style={'textAlign':'center'}),
        html.Div(style={'textAlign':'center'},
            children='''
            Built with Dash, a web app framework for Python.
            '''),
        #scatterplot
        dcc.Graph(
            id='water-viz-w-checkbox',
            figure={
                'data': [
                    go.Scatter(
                        x=df[df['SchoolCounty'] == i]['SchoolName'],
                        y=df[df['SchoolCounty'] == i]['RESULT'],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name=i
                    ) for i in df['SchoolCounty'].unique()
                ],
                'layout': go.Layout(
                    xaxis={'title': 'SchoolName'},
                    yaxis={'title': 'RESULT'},
                    margin={'l': 200, 'b': 40, 't': 100, 'r': 200},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        ),
    
        dcc.Slider(
        id='amount-slider',
        min=df['RESULT'].min(),
        max=df['RESULT'].max(),
        value=df['RESULT'].min(),
        marks={str(RESULT): str(RESULT) for RESULT in df['RESULT'].unique()}
        ),

        
        #styled table
        dash_table.DataTable(
            id='table',
            columns=[
                {"id": i,
                 "name": i} 
                 for i in df.columns if i in selected],
            data=df.to_dict("rows"),
            # row_selectable=True,
            # filterable=True,
            # sortable=True,
            style_table={
                'maxHeight': '300px',
                'overflowY': 'scroll',
                'border': 'thin lightgrey solid'
            },
            style_cell={
                'minWidth': '0px', 
                'maxWidth': '180px',
                'whiteSpace': 'normal',
                'whiteSpace': 'no-wrap',
                'textOverflow': 'ellipsis',
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
            style_cell_conditional=[
                {'if': {'column_id': 'ID'},
                'width': '5%'},
                {'if': {'column_id': 'Temperature'},
                'width': '35%'},
                {'if': {'column_id': 'WaterSystemCounty'},
                'width': '25%'},
                {'if': {'column_id': 'SchoolName'},
                'width': '30%'},
                {'if': {'column_id': 'RESULT'},
                'width': '25%'}, 
            ]
        ),

        #coming soon - map,
        fig = ff.create_choropleth(
            fips=fips, values=values, scope=['California'], show_state_data=True,
            colorscale=colorscale, binning_endpoints=[5, 101, 500, 700, 9000], round_legend_values=True,
            plot_bgcolor='rgb(229,229,229)',
            paper_bgcolor='rgb(229,229,229)',
            legend_title='Highest Lead record by County',
            county_outline={'color': 'rgb(255,255,255)', 'width': 1.0},
            exponent_format=True,
        )

        py.iplot(fig, filename='choropleth_california_lead')
        # dcc.Checklist(
        #     options=[
        #         {'label': 'New York City', 'value': 'NYC'},
        #         {'label': u'Montréal', 'value': 'MTL'},
        #         {'label': 'San Francisco', 'value': 'SF'}
        #     ],
        #     values=['MTL', 'SF']
        # ), 
]

)

if __name__ == '__main__':
    app.run_server(debug=True)
