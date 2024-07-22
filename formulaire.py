from dash import Dash, html
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import os

    
def get_df(relative_path):
    #retrouve le chemin du dossier dash_site_dps
    path = os.path.dirname(os.path.realpath(__file__))
    
    #retourne la dataframe choisi via son relative path
    return pd.read_csv(path + relative_path).iloc[:,1:-1]

def create_formulaire(df):
    return [html.P(f"{df.columns}"), html.P(f"{df.dtypes.values}")]