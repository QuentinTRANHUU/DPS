from dash import Dash, html
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import os

    
def get_df(relative_path):
    #retrouve le chemin du dossier dash_site_dps
    path = os.path.dirname(os.path.realpath(__file__))
    
    #retourne la dataframe choisi via son relative path
    
    if relative_path ==  r"\dataframes\chd_clean.csv":
        df = pd.read_csv(path + relative_path, dtype = {'sex': "object", 
                                                         'fbs': "object", 
                                                         'exang': "object", 
                                                         'cp': "object", 
                                                         'restecg': "object", 
                                                         'slope': "object", 
                                                         'ca' : "object", 
                                                         'thal': "object"})
    else:
        df = pd.read_csv(path + relative_path)
    
    return pd.read_csv(path + relative_path)

def create_champ_formulaire(df,col,page_name, col_name):
    
    col_type = df[col].dtype
    if col_type == "O" or (col_type == "int64" and len(df[col].unique()) < 7) :
        return dbc.InputGroup(
                            [
                                dbc.InputGroupText(col_name[page_name][col]),
                                dbc.Select(options=[{"label": val, "value": val} for val in df[col].unique()],
                                           id = {"type": page_name+"_form_input", "index": page_name+"_"+col})
                            ],
                            className="mb-3"
                            )
    else :
        return dbc.InputGroup(
                                [
                                    dbc.InputGroupText(col_name[page_name][col]),
                                    dbc.Input(type="number",
                                           id = {"type": page_name+"_form_input", "index": page_name+"_"+col})
                                ],
                                className="mb-3"
                            )

def create_formulaire(df, page_name, col_name):
    champs_a_remplir = [html.Div([create_champ_formulaire(df, col, page_name, col_name) for col in df.iloc[:,:-1].columns])]
    submit_button = [dbc.Row(dbc.Col(html.Div(dbc.InputGroup(
                            [
                                dbc.Button("Tester",
                                           color="primary",
                                           className="mb-3",
                                           id = page_name + "_submit_button")
                            ],
                            className="mb-3"
                            )),width={"offset": 9}))]
    resultats = [dbc.Card(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.CardBody(
                                                html.H2("Votre résultat", className="card-title text-center p-4"),
                                                id = page_name + "_resultat"
                                        ),
                                        className="col-md-8",
                                        width={"offset":2}
                                    ),
                                ],
                                className="bg-warning text-white g-0 d-flex align-items-center",
                            )
                        ])]
    return  champs_a_remplir + submit_button + resultats