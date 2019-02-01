""" 
base items to install on the computer

pip install dash==0.21.1 # The core dash backend
pip install dash-renderer==0.12.1 # The dash front-end
pip install dash-html-components==0.10.1 # HTML components
pip install dash-core-components==0.22.1 # Supercharged components
pip install plotly --upgrade 

"""
#Resources: Basic Tutorials
#https://medium.freecodecamp.org/this-quick-intro-to-dash-will-get-you-to-hello-world-in-under-5-minutes-86f8ae22ca27
#https://www.datacamp.com/community/tutorials/learn-build-dash-python
#https://towardsdatascience.com/how-to-create-your-first-web-app-using-python-plotly-dash-and-google-sheets-api-7a2fe3f5d256


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

header_names =[ 'SchoolName', 'SchoolCounty', 'RESULT', 'class']
df = pd.read_csv('./filtered.csv', names=header_names)

colors = {
         'background': '#0000FF',
         'color': '#FFA500'}

#External CSS
external_css = ["https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
                "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css", ]
for css in external_css:
    app.css.append_css({"external_url": css})

#External JS
external_js = ["http://code.jquery.com/jquery-3.3.1.min.js",
               "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"]
for js in external_js:
    app.scripts.append_script({"external_url": js})


#app Layout
app.layout = html.Div(style=colors,children=[
    html.H1(children='water visualization',style={'textAlign':'center'}),
html.Div(style={'textAlign':'center'},children='''
     Built with Dash: A web application framework for Python.
    ''')
])

#scatterplot
dcc.Graph(
        id='water Viz',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['class'] == i]['SchoolName'],
                    y=df[df['class'] == i]['RESULT'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df['class'].unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'SchoolName'},
                yaxis={'title': 'RESULT'},
                margin={'l': 200, 'b': 40, 't': 100, 'r': 200},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )

if __name__ == '__main__':
    app.run_server(debug=True)