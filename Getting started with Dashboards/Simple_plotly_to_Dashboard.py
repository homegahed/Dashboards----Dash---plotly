# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 12:01:48 2022

@author: Hossam Megahed
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np 


app = dash.Dash()
#setting seed for generting random numbers

np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div([dcc.Graph(id='scatterplot', 
                                 figure={'data':[
                                     go.Scatter(
                                         x=random_x,
                                         y=random_y,
                                         mode='markers',
                                         marker={'size':12,
                                                 'color': 'rgb(51, 204, 153)',
                                                 'symbol':'pentagon',
                                                 'line':{'width':2}}
                                         )],
                                         'layout':go.Layout(
                                             title='My Scatterplot',
                                             xaxis={'title': 'some X title'}
                                             )}),
                       dcc.Graph(id='scatterplot2', 
                                    figure={'data':[
                                        go.Scatter(
                                            x=random_x,
                                            y=random_y,
                                            mode='markers',
                                            marker={'size':12,
                                                    'color': 'rgb(70, 50, 153)',
                                                    'symbol':'pentagon',
                                                    'line':{'width':2}}
                                            )],
                                            'layout':go.Layout(
                                                title='My 2nd Scatterplot',
                                                xaxis={'title': 'some X title'}
                                                )})

    ])


if __name__ == '__main__':
    app.run_server()