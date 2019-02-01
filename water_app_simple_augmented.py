""" 
TO DO: move these to a requirements.txt file

pip install dash==0.21.1 # The core dash backend
pip install dash-renderer==0.12.1 # The dash front-end
pip install dash-html-components==0.10.1 # HTML components
pip install dash-core-components==0.22.1 # Supercharged components
pip install dash-table==3.1.11
pip install plotly --upgrade 

"""
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
import plotly.graph_objs as go



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

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

#app Layout

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
        #table
        html.H1(children='Data Table',
                style={'textAlign':'center'}
                ),
        generate_table(df),
        
        #styled table
        dash_table.DataTable(
            id='table',
            columns=[{"ID": i, "WaterSystemCounty": i, "SchoolName": i, "RESULT": i} for i in df.columns],
            data=df.to_dict("rows"),
            style_table={
                'maxHeight': '300px',
                'overflowY': 'scroll',
                'border': 'thin lightgrey solid'
            },
            style_cell={
                'minWidth': '0px', 
                'maxWidth': '180px',
                'whiteSpace': 'normal'
                #'whiteSpace': 'no-wrap',
                #'textOverflow': 'ellipsis',
            },
            css=[{
                'selector': '.dash-cell div.dash-cell-value',
                'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
            }],
            style_cell_conditional=[
                {'if': {'column_id': 'ID'},
                'width': '30%'},
                {'if': {'column_id': 'Temperature'},
                'width': '30%'},
                {'if': {'column_id': 'WaterSystemCounty'},
                'width': '30%'},
                {'if': {'column_id': 'SchoolName'},
                'width': '30%'},
                {'if': {'column_id': 'RESULT'},
                'width': '30%'},
            ] 
        ),

        #coming soon - map,
       """  dcc.Checklist(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            values=['MTL', 'SF']
        ),  """
]

)

if __name__ == '__main__':
    app.run_server(debug=True)