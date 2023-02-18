from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from components import dashboards, sidebar ,extratos


import app as app

from app import *




# =========  Layout  =========== #
content = html.Div(id="page-content")


# dbc.Row - linha da pagina para layout
# dbc.Col - colunas das paginas

app.layout = dbc.Container(children=[
    dbc.Row([
    dbc.Col([ dcc.Location(id="url"),
              sidebar.layout
    ],md=2),
    dbc.Col([
        content
    ],md=10)
])



], fluid=True,)

# callback para fixar a sidebar e mudar o conteudo
@app.callback(Output('page-content', 'children'), [Input('url','pathname')])

# função para mudar o content da page conforme o path(caminho)
def render_page(pathname):
    
        if pathname == '/' or pathname == '/dashboard':
            return dashboards.layout

        if pathname == '/extratos':
            return extratos.layout
        



#Running no server e a porta 
# debug true - a cada salvamento a alteracaoi no site e automatica|| false -a atualização do site manualmente
if __name__ == '__main__':
    app.run_server(port=8051, debug=True)