import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df=pd.read_csv('data/cleaned_spacex_falcon9.csv')
app=Dash(__name__)
app.layout=html.Div([
 html.H1('Falcon 9 Landing Analytics'),
 dcc.Dropdown(id='site',options=[{'label':s,'value':s} for s in sorted(df.LaunchSite.unique())],
              value='CCAFS SLC 40',clearable=False),
 dcc.Graph(id='pie'),
 dcc.Graph(id='scatter')
])
@app.callback(Output('pie','figure'),Output('scatter','figure'),Input('site','value'))
def update(site):
 d=df[df.LaunchSite==site]
 pie=px.pie(d,names=d['Class'].map({0:'Failure',1:'Success'}),title='Landing outcome')
 scatter=px.scatter(d,x='PayloadMass',y='Class',hover_data=['FlightNumber','Orbit'],
                    title='Payload mass vs landing outcome')
 return pie,scatter
if __name__=='__main__': app.run(debug=True)
