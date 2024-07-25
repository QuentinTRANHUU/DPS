from dash import html, register_page
import dash_bootstrap_components as dbc

# Enregistrement de la page
register_page(__name__)

# Créez la mise en page
layout = dbc.Container([

    #------------------------Contact--------------------------#
    
    dbc.Row([
        dbc.Col(
                dbc.Card(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.CardImg(
                                        src=r"\assets\images\facteur_chat.jpg",
                                        className="img-fluid rounded-start",
                                    ),
                                    className="col-md-6",
                                ),
                                dbc.Col(
                                    dbc.CardBody(
                                        [
                                            html.H4("Contact", className="card-title text-center p-2"),
                                            html.P(
                                                "Email : data.avengers@dps.fr",
                                                className="card-text"
                                            ),
                                            html.P(
                                                "Telephone : 06 12 12 12 12",
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
                            className="bg-secondary bg-opacity-50 text-black g-0 d-flex align-items-center",
                        )
                    ],
    className="m-5",
    ),
    width= {"size":8,"offset":2})
    ]),
])
    #-------------Formulaire de questions ---------------#
