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