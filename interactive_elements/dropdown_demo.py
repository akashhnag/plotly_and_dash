import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as  px
import pandas as pd
import numpy as np

education = pd.read_csv("states_all.csv").assign(
    expenditure_per_student = lambda x: x["TOTAL_EXPENDITURE"] / x["GRADES_ALL_G"],
    above_avg_math8 = lambda x: np.where(x["AVG_MATH_8_SCORE"] > 278.6,'Above Avg', 'Below Avg')
)


app= dash.Dash(__name__)

app.layout=html.Div([
    dcc.Dropdown(
        id="filter",
        options=["CALIFORNIA","TEXAS"],
        value=["CALIFORNIA"]
    ),
    dcc.Graph(id="graph")
])

@app.callback(Output('graph','figure'),
              Input('filter','value'))

def  plot_rev_scatter(state):
    fig=px.line(
        (
            education.query("STATE in @state and 1992 < YEAR < 2016")
            .groupby("YEAR")
            .sum()
            .reset_index()
        ),
        x='YEAR',
        y='TOTAL_EXPENDITURE',
        title=f"Expenditure OVer Time, Selected States",
    )
    return fig

if __name__=="__main__":
    app.run_server(debug=True)