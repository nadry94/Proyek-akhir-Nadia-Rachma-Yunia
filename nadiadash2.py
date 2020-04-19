import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns
import csv

from dash.dependencies import Input,Output, State

jtg=pd.read_csv('C:/Users/nadia/python nadia/PROYEK AKHIR/heart.csv')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[html.H1('Dash Nadia'),
                                html.Div(children='''Heart Disease Classification'''),
                                html.Div([dcc.Tabs([dcc.Tab(children =[html.Div([ html.Div([html.P('x-axis'), dcc.Dropdown(value ='None', id = 'filter-xaxis',
                                                                                                                             options = [{'label' : 'Age', 'value' : 'age'},
                                                                                                                                        {'label' : 'Sex', 'value' : 'sex'},
                                                                                                                                        {'label' : 'Chest Pain Type', 'value' : 'cp'},
                                                                                                                                        {'label' : 'Resting Blood Pressure', 'value' : 'trestbps'},
                                                                                                                                        {'label' : 'Serum Cholesterol', 'value' : 'chol'},
                                                                                                                                        {'label' : 'Fasting Blood Sugar', 'value' : 'fbs'},
                                                                                                                                        {'label' : 'Resting ECG result', 'value' : 'restecg'},
                                                                                                                                        {'label' : 'Maximum Heart Rate Achieved', 'value' : 'thalach'},
                                                                                                                                        {'label' : 'Exercise Induced Angina (1 = yes; 0 = no)', 'value' : 'exang'},
                                                                                                                                        {'label' : 'Depression induced by exercise relative to rest', 'value' : 'oldpeak'},
                                                                                                                                        {'label' : 'Slope', 'value' : 'slope'},
                                                                                                                                        {'label' : 'Number of Major vessels (0-3) colored by flourosopy', 'value' : 'ca'},
                                                                                                                                        {'label' : 'Thalassemia', 'value' : 'thal'},
                                                                                                                                        {'label' : 'Target (0=no, 1=yes)', 'value' : 'target'},
                                                                                                                                        {'label' : 'None', 'value' : 'None'}
                                                                                                                                       ]
                                                                                                                            )
                                                                                            
                                                                                                               ], className = 'col-12'),
                                                                                                               
                                                                                                      html.Div([html.P('y-axis'),
                                                                                                                dcc.Dropdown(value = 'None', id = 'filter-yaxis', 
                                                                                                                             options=[{'label' : 'Age', 'value' : 'age'},
                                                                                                                                      {'label' : 'Sex', 'value' : 'sex'},
                                                                                                                                      {'label' : 'Chest Pain Type', 'value' : 'cp'},
                                                                                                                                      {'label' : 'Resting Blood Pressure', 'value' : 'trestbps'},
                                                                                                                                      {'label' : 'Serum Cholesterol', 'value' : 'chol'},
                                                                                                                                      {'label' : 'Fasting Blood Sugar', 'value' : 'fbs'},
                                                                                                                                      {'label' : 'Resting ECG result', 'value' : 'restecg'},
                                                                                                                                      {'label' : 'Maximum Heart Rate Achieved', 'value' : 'thalach'},
                                                                                                                                      {'label' : 'Exercise Induced Angina (1 = yes; 0 = no)', 'value' : 'exang'},
                                                                                                                                      {'label' : 'Depression induced by exercise relative to rest', 'value' : 'oldpeak'},
                                                                                                                                      {'label' : 'Slope', 'value' : 'slope'},
                                                                                                                                      {'label' : 'Number of Major vessels (0-3) colored by flourosopy', 'value' : 'ca'},
                                                                                                                                      {'label' : 'Thalassemia', 'value' : 'thal'},
                                                                                                                                      {'label' : 'Target (0=no, 1=yes)', 'value' : 'target'},
                                                                                                                                      {'label' : 'None', 'value' : 'None'}
                                                                                                                                     ]
                                                                                                                            )
                                                                                                               ], className = 'col-12'),
                                
                                                                                                               ], className ='row'),
                                                                                                    html.Br(),
                                                                                                    html.Div(children=[html.Button('Create the plot', id = 'create_bar')],className = 'row col-3'),

                                                                                                    html.Br(),
                                                                                                    html.Div(id='show_graph', children = dcc.Graph(id='graphs_bar'))]
                                                                                                    
                                                                                                    )])])])


@app.callback(Output (component_id ='show_graph', component_property = 'children'),
              [Input (component_id ='create_bar', component_property = 'n_clicks')],
              [State (component_id ='filter-xaxis', component_property = 'value'),
               State (component_id ='filter-xaxis', component_property = 'value')]
             )

def create_bar_plot(n_clicks,f_xaxis,f_yaxis):
    if((f_xaxis == 'None') or (f_xaxis=='') or (f_xaxis=='Null')) or   ((f_yaxis == 'None') or (f_yaxis=='') or (f_yaxis=='Null')):
        return ''
    else:
         bar_stream = dcc.Graph(id = 'graph-bar', figure = {'data' : [{'x' : jtg[f_xaxis],
                                                                      'y' : jtg[f_yaxis],
                                                                      'type' : 'bar',
                                                                      'name' : '{}-{}'.format(f_xaxis, f_yaxis)
                                                                      }],
                                                            'layout' : go.Layout(xaxis = {'title' : '{}'.format(f_xaxis)},
                                                                                 yaxis = {'title' : '{}'.format(f_yaxis)},
                                                                                 title = 'Heart Disease Visualization',
                                                                                 hovermode = 'closest'
                                                                                 )
                                                          }
                              )
    return bar_stream
                 

if __name__ == '__main__':
    app.run_server(debug=True)