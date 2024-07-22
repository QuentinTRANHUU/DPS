from dash import Dash, html, dcc,register_page
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import os

path = os.path.dirname(os.path.realpath(__file__))
my_path = '\\'.join(path.split('\\')[:-1])

os.chdir(path=my_path)

df = pd.read_csv(my_path + r"\dataframes\clean_ckd_df.csv")

# Enregistrement de la page
register_page(__name__)

# Créez la mise en page
layout = dbc.Container([
    
    #------------------------Nom Page--------------------------#
    dbc.Row([
        dbc.Col(html.H1("Maladie Rénale Chronique",
                        className="text-black p-4 text-center"))
    ]),
    
    #------------------------Avant de commencer--------------------------#
    
    dbc.Row([
        dbc.Col(width= 3),
        dbc.Col(
                dbc.Card(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.CardImg(
                                        src=r"\assets\images\doctor.jpg",
                                        className="img-fluid rounded-start",
                                    ),
                                    className="col-md-4",
                                ),
                                dbc.Col(
                                    dbc.CardBody(
                                        [
                                            html.H4("Avant de commencer", className="card-title text-center p-4"),
                                            html.P(
                                                f"Afin de pouvoir procéder au test, veuillez vous munir au préalable des informations suivantes :\n\
                                                {[col for col in df.columns][:-1]}",
                                                className="card-text",
                                            )
                                        ]
                                    ),
                                    className="col-md-8",
                                ),
                            ],
                            className="bg-warning text-black g-0 d-flex align-items-center",
                        )
                    ],
    className="mb-3",
    ),
            width= 6)
    ]),

    #------------------------Faites le Test--------------------------#

    dbc.Row([
        dbc.Col(width= 3),
        dbc.Col(
                
                dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            [
                                html.P(f"{df.columns}")
                            ],
                            title=html.H4("Faites le Test", className="text-center"),
                            className="bg-light")
                    ],
                    start_collapsed=True
                    ),
                className="mb-3",
                width= 6)
    ])
])