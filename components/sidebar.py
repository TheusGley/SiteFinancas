import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app


from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd






# ========= Layout ========= #
layout = dbc.Col([
            html.H1("Usuario", className="text-primary"),
            html.P("by Matheus", className="text-info"),
            html.Hr(),
            
    
    
#=======================Seção de perfil====================
        
        
        # imagem de perfil
        dbc.Button(id="botao_perfil",
                   children=[html.Img(src='/assets/img_hom.png', id='avatar_change',alt='Avatar', className='perfil_avatar')],
                   style={'background': 'transparent', 'border-color':'tansparent'}),
                
            

# =========Seção nova=====

#botoes de Nova receita ou despesa

dbc.Row([
                dbc.Col([
                    dbc.Button(color='success', id='open-novo-receita',
                        children=['+Receita'])
                    
                    
                ],width=6),
                
                dbc.Col([
                    dbc.Button(color='danger', id='open-novo-despesa',
                        children=['-Despesa'])
                    
                    
                ],width=6)
                    
                ]),

        # ===============   Modals   =========== #
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('Adicionar Receita')),
                    dbc.ModalBody(dbc.Row([
                                            dbc.Col([
                                                dbc.Label('Descrição '),
                                                dbc.Input(placeholder="Ex.:Dividendos da bolsa, herança, outros...", id="txt-receita")
                                                        ],width=6),
                                            dbc.Col([
                                                dbc.Label("Valos: "),
                                                dbc.Input(placeholder="$100.00", id="valor_receita", value="")
                                                ],width=6)
                                        ]),
                                        dbc.Row([
                                            dbc.Col([
                                                dbc.Label("Data: "),
                                                dcc.DatePickerSingle(id="date-receitas",
                                                    min_date_allowed=date(2020,1,1),
                                                    max_date_allowed=date(2030,12,31),
                                                    date = datetime.today(),
                                                    style={"width":"100%"}
                                            ),
                                                
                                            ])
                                        ])
                                  ),
                ],id="modal-novo-receita"),
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle('Adicionar Despesa')),
                    dbc.ModalBody(),
                ],id="modal-novo-despesa"),
                
                # ===================   Nova seção  NAV   ================== #
#barra de navegação

html.Hr(),

dbc.Nav([
   dbc.NavLink('Dashboard', href="/dashboards", active="exact"),
   dbc.NavLink('Extratos', href="/extratos", active="exact"),
   
   ],vertical=True, pills=True, id='nav_buttons',style={"margin-bottom": "50px"}),




])


# =========  Callbacks  =========== #


# Pop-up receita
@app.callback(
    Output('modal-novo-receita','is_open'),
    Input('open-novo-receita','n_clicks'),
    State('modal-novo-receita','is_open')
)
def toggle_modal(n1,is_open):
    if n1:
        return not is_open 
    
    # Pop-up despesa
@app.callback(
    Output('modal-novo-despesa','is_open'),
    Input('open-novo-despesa','n_clicks'),
    State('modal-novo-despesa','is_open')
)
def toggle_modal(n1,is_open):
    if n1:
        return not is_open 