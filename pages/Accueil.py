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
        dbc.Col(html.H1("Accueil",
                        className="text-black p-4 text-center"))
    ]),

    
    #------------------------Le monde va mal--------------------------#
    
    dbc.Row([
        dbc.Col(width= 3),
        dbc.Col(
                dbc.Card(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.CardBody(
                                        [
                                            html.H4("Le monde va mal", className="card-title text-center p-4"),
                                            html.P(
                                                "blabalbalbalaipoehfagçfdaohdfghblabalbalbalaipoehfagçfdaohdfghblabalbalbalaipoehfagçfdaohdfgh",
                                                className="card-text",
                                            )
                                        ]
                                    ),
                                    className="col-md-8",
                                ),
                                
                                dbc.Col(
                                    dbc.CardImg(
                                        src=r"\assets\images\doctor.jpg",
                                        className="img-fluid rounded-start",
                                    ),
                                    className="col-md-4",
                                )
                            ],
                            className="bg-dark text-white g-0 d-flex align-items-center",
                        )
                    ],
    className="mb-3",
    ),
            width= 7),
        dbc.Col(width= 2)
    ]),
    dbc.Row(style={"height": "5vh"}),

    #------------------------présentation--------------------------#
    
    dbc.Row([
        dbc.Col(width= 2),
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
                                            html.H4("Qui sommes-nous ?", className="card-title text-center p-4"),
                                            html.P(
                                                "blabalbalbalaipoehfagçfdaohdfghblabalbalbalaipoehfagçfdaohdfghblabalbalbalaipoehfagçfdaohdfgh",
                                                className="card-text",
                                            )
                                        ]
                                    ),
                                    className="col-md-8",
                                ),
                            ],
                            className="bg-secondary text-black g-0 d-flex align-items-center",
                        )
                    ],
    className="mb-3",
    ),
            width= 7),
        dbc.Col(width= 3)
    ]),
    dbc.Row(style={"height": "5vh"}),
    
    #------------------------Nos valeurs--------------------------#
    
    dbc.Row([
        dbc.Col(width= 3),
        dbc.Col(
                dbc.Card(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.CardBody(
                                        [
                                            html.H4("Nos valeurs", className="card-title text-center p-4"),
                                            html.P(
                                                "blabalbalbalaipoehfagçfdaohdfghblabalbalbalaipoehfagçfdaohdfghblabalbalbalaipoehfagçfdaohdfgh",
                                                className="card-text",
                                            )
                                        ]
                                    ),
                                    className="col-md-8",
                                ),
                                
                                dbc.Col(
                                    dbc.CardImg(
                                        src=r"\assets\images\doctor.jpg",
                                        className="img-fluid rounded-start",
                                    ),
                                    className="col-md-4",
                                )
                            ],
                            className="bg-primary text-white g-0 d-flex align-items-center",
                        )
                    ],
    className="mb-3",
    ),
            width= 7),
        dbc.Col(width= 2)
    ]),
    dbc.Row(style={"height": "5vh"}),

    #------------------------Notre Solution--------------------------#
    
    dbc.Row([
        dbc.Col(width= 2),
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
                                            html.H4("Notre Solution", className="card-title text-center p-4"),
                                            html.P(
                                                "blabalbalbalaipoehfagçfdaohdfghblabalbalbalaipoehfagçfdaohdfghblabalbalbalaipoehfagçfdaohdfgh",
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
            width= 7),
        dbc.Col(width= 3)
    ]),
    
    dbc.Row(style={"height": "5vh"}),
    
    #------------------------Avis--------------------------#

    dbc.Row([
                dbc.Col(width = 3),
                dbc.Col(html.H1("Ils témoignent",
                                className="bg-info text-black p-4 text-center"),
                        width = 6)
    ]),

    dbc.Row([
                dbc.Col(width = 3),
                dbc.Col(dbc.Carousel(
                            items=[
                                {"key": "1", "caption" : "Des problèmes urinaires ? Vous n'êtes pas seuls !" , "src": r"/assets/images/ex_carrou_1.jpeg"},
                                {"key": "2", "src": r"/assets/images/ex_carrou_2.jpeg"},
                                {"key": "3", "src": r"/assets/images/ex_carrou_3.jpeg"},
                                {"key": "4", "src": r"\assets\images\doctor.jpg"},
                            ],
                            controls=True,
                            indicators=True
                            ),
                        width = 6)
            ])
])