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
        dbc.Col(html.H1("Informations",
                        className="text-black p-4 text-center"))
    ]),

    #------------------------Contact--------------------------#
    
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
                                            html.H4("Contact", className="card-title text-center p-4"),
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
])