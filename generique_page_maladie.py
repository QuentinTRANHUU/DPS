from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import formulaire


def create_layout(df_relative_path,page_name):

    df = formulaire.get_df(df_relative_path)

    # Créez la mise en page
    return dbc.Container([
        
        #------------------------Nom Page--------------------------#
        dbc.Row([
            dbc.Col(html.H1(page_name,
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
                                                    {[col for col in df.columns]}",
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
                            formulaire.create_formulaire(df),
                            title=html.H4("Faites le Test", className="text-center"),
                                className="bg-light")
                        ],
                        start_collapsed=True
                        ),
                    className="mb-3",
                    width= 6)
        ])
    ])