import pandas as pd
import plotly.express as px
from dash import Dash,dcc

spain_skiers=pd.read_csv('spanish_skiers.csv')

app=Dash()

fig=px.line(
    spain_skiers,
    x='Year',
    y='Percent_Skiers',
    labels={"Percent_Skiers":"Percentage of Spainiard that skied"},
    title="Percent of Spanish who skied each year"
    )

app.layout=[
    dcc.Graph(id='line-chart',figure=fig)
]

if __name__=='__main__':
    app.run_server(debug=True)
