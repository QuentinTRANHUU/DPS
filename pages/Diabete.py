from dash import Dash, html, dcc,register_page
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Enregistrement de la page
register_page(__name__)

# Créez la mise en page
layout = dbc.Container([
    
    #------------------------Nom Page--------------------------#
    dbc.Row([
        dbc.Col(html.H1("Diabète",
                        className="text-black p-4 text-center"))
    ]),
])