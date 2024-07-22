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
                                                "Afin de pouvoir procéder au test, veuillez vous munir au préalable des informations suivantes :\n\
                                                blabla mesure 1 etc....",
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
                                html.P("This is the content of the first section"),
                                dbc.Button("Click here"),
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