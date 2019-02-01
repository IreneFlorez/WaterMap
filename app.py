# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import json

import sys
sys.path.append('schools_db/')
from school_info import school_info_obj

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

school = school_info_obj("Saratoga Special Services Preschool")
# school1_json_obj = json.dumps((school1_json))
# print(school1_json_obj)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),

    html.H1(children='Take Action'),
    html.P(children=school.school),
    html.P(children=school.county + " County"),
    html.P(children=school.district + " School District"),
    html.P(children=school.admin_first_name + " "+ school.admin_last_name),
    html.P(children=school.admin_email)

])

if __name__ == '__main__':
    app.run_server(debug=True)