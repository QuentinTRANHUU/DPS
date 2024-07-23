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
                                                "Les maladies chroniques, telles que le diabète, les maladies cardiovasculaires,les maladies rénales et les maladies hépatiques, touchent des millions de personnes chaque année. Malgré les avancées médicales, trop de diagnostics sont posés tardivement, compromettant la qualité de vie et augmentant les coûts de traitement. Il est primordial d'inverser cette tendance préoccupante",
                                                className="card-text",
                                            )
                                        ]
                                    ),
                                    className="col-md-8",
                                ),
                                
                                dbc.Col(
                                    dbc.CardImg(
                                        src=r"\assets\images\ACCUEIL_le_monde_va_mal.png",
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
                                        src=r"\assets\images\ACCUEIL_Qui_sommes_nous.png",
                                        className="img-fluid rounded-start",
                                    ),
                                    className="col-md-4",
                                ),
                                dbc.Col(
                                    dbc.CardBody(
                                        [
                                            html.H4("Qui sommes-nous ?", className="card-title text-center p-4"),
                                            html.P(
                                                "Nous sommes une équipe de professionnels de la data unis par une mission commune : transformer la prévention des maladies chroniques. Nous avons développé des outils de dépistage avancés qui permettent de détecter les signes avant-coureurs de maladies avant qu'elles ne deviennent critiques. Notre objectif est d'offrir à chacun la possibilité de prendre en main sa santé grâce à des solutions fiables et accessibles",
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
                                                "Précision : Chaque diagnostic est basé sur des données cliniques rigoureusement validées par des experts.",
                                                className="card-text"
                                                ),
                                            html.P(
                                                "Accessibilité : Nous croyons que chaque individu mérite un accès égal aux outils de dépistage de pointe, indépendamment de sa situation géographique ou socio-économique."
                                                ,className="card-text"
                                                ),
                                            html.P(
                                                "Innovation : Nous sommes constamment à la recherche de nouvelles méthodes pour améliorer nos technologies et offrir des solutions toujours plus efficaces."
                                                ,className="card-text"
                                                ),
                                            html.P(
                                                "Compassion : Nous plaçons l'humain au cœur de notre démarche, en prenant soin de chaque patient avec respect et empathie."
                                                ,className="card-text"
                                                )

                                        ]
                                    ),
                                    className="col-md-8",
                                ),
                                
                                dbc.Col(
                                    dbc.CardImg(
                                        src=r"\assets\images\ACCUEIL_Nos_valeurs.png",
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
                                        src=r"\assets\images\ACCUEIL_Notre_solution.png",
                                        className="img-fluid rounded-start",
                                    ),
                                    className="col-md-4",
                                ),
                                dbc.Col(
                                    dbc.CardBody(
                                        [
                                            html.H4("Notre Solution", className="card-title text-center p-4"),
                                            html.P(
                                                "Notre solution repose sur un modèle de prédiction avancé, conçu pour identifier les risques de maladies chroniques avec une précision inégalée. En combinant des algorithmes d'intelligence artificielle avec des données cliniques actualisées, nous offrons un dépistage personnalisé qui tient compte de l'historique médical, des habitudes de vie, et des facteurs génétiques de chaque individu. Grâce à notre plateforme intuitive, vous pouvez réaliser un dépistage complet en quelques clics et recevoir des recommandations personnalisées pour prévenir les complications. Ensemble, transformons la prévention et faisons de la santé une priorité accessible à tous",
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