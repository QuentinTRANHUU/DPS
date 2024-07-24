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
    dbc.Col(),
    dbc.Col(
        dbc.Card(
            dbc.CardBody(
                        html.H2("Informations",
                                className="card-title text-black text-center p-2")
                        ),
            className="bg-light"),
        width = {"size" : "auto"}
        ),
    dbc.Col(),
    ],
    className="m-5"),

    #------------------------Contact--------------------------#
    
    dbc.Row([
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
                                    className="col-md-6",
                                ),
                                dbc.Col(
                                    dbc.CardBody(
                                        [
                                            html.H4("Contact", className="card-title text-center p-2"),
                                            html.P(
                                                "Email : datapowerscreening@gmail.com",
                                                className="card-text"
                                            ),
                                            html.P(
                                                "Telephone : 06 03 15 48 78",
                                                className="card-text"
                                            ),
                                            html.P(
                                                "Adresse : 221B Baker Street, Londres",
                                                className="card-text"
                                            )
                                        ]
                                    ),
                                    className="col-md-6",
                                ),
                            ],
                            className="bg-warning text-black g-0 d-flex align-items-center",
                        )
                    ],
    className="mb-3",
    ),
    width= {"size":8,"offset":2})
    ]),
])
    #-------------Formulaire de questions ---------------#
