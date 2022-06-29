# Uses a dropdown list to control the year of the chart
import dash
from dash.dependencies import Output, Input
from dash import no_update
from dash import dcc
from dash import html                       

import pandas as pd 
import plotly.express as px

diabetes = pd.read_csv('https://bitbucket.org/jimcody/sampledata/raw/b2aa6df015816ec35afc482b53df1b7ca7a31f80/diabetes_for_plotly.csv')
d_month = diabetes.groupby(['year','month']).sum().reset_index()
d_month = d_month.sort_values(['year','month'])

fig5 = px.line(d_month,x='month', y='num_medications')

####### Build the App. ##################
app = dash.Dash(__name__) 
server = app.server

app.layout = html.Div([
    
    dcc.Graph(id='x', figure = fig5),   # Don't forget the comma
    
    dcc.Dropdown(id='dropdown', 
                 options=[
                {'label': i, 'value': i} for i in d_month.year.unique()
                ],  value=2019,
                    clearable=False,placeholder='Filter by year...')
    
])


@app.callback(
   
    Output('x', 'figure'),
    Input('dropdown', 'value'))

def update_figure(selected_year):
    d_month2 = d_month[d_month.year == selected_year]
    
    fig5 = px.line(d_month2,x='month', y='num_medications')
    fig5.update_layout(transition_duration=100)
    return fig5

if __name__ == '__main__':
    app.run_server(debug=True)