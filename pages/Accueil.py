from dash import html,register_page
import dash_bootstrap_components as dbc

# Enregistrement de la page
register_page(__name__, path='/')

# Créez la mise en page
layout = dbc.Container([
    
    #------------------------Le monde va mal--------------------------#
    
    dbc.Row([
        dbc.Col(
                dbc.Card(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.CardBody(
                                        [
                                            html.H4("Le monde va mal", className="card-title text-center p-2"),
                                            html.P(
                                                "Les maladies chroniques, telles que le diabète, les maladies cardiovasculaires, les maladies rénales et les maladies hépatiques, touchent des millions de personnes chaque année. Malgré les avancées médicales, trop de diagnostics sont posés tardivement, compromettant la qualité de vie et augmentant les coûts de traitement. Il est primordial d'inverser cette tendance préoccupante",
                                                className="card-text",
                                            )
                                        ]
                                    ),
                                    className="col-md-6",
                                ),
                                
                                dbc.Col(
                                    dbc.CardImg(
                                        src=r"\assets\images\ACCUEIL_le_monde_va_mal.png",
                                        className="img-fluid rounded-start",
                                    ),
                                    className="col-md-6",
                                )
                            ],
                            className="bg-dark text-white g-0 d-flex align-items-center text-center",
                        )
                    ],
                    className="m-5"
                    ),
             width= {"size":11,"offset":0})
    ]),
    dbc.Row(style={"height": "5vh"}),

    #------------------------présentation--------------------------#
    
    dbc.Row([
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
                                    className="col-md-6",
                                ),
                                dbc.Col(
                                    dbc.CardBody(
                                        [
                                            html.H4("Qui sommes-nous ?", className="card-title text-center p-2"),
                                            html.P(
                                                "Nous sommes une équipe de Data Analysts unis par une mission commune, transformer la prévention des maladies chroniques par le développement de puissants algorithmes de dépistage des maladies. Notre objectif : vous offrir une longueur d'avance sur la maladie.",
                                                className="card-text",
                                            )
                                        ]
                                    ),
                                    className="col-md-6",
                                ),
                            ],
                            className="bg-secondary  bg-opacity-50 text-black g-0 d-flex align-items-center  text-center",
                        )
                    ],
    className="mb-3",
    ),
    width= {"size":11,"offset":1}),
    ]),
    dbc.Row(style={"height": "5vh"}),

    #------------------------Notre Solution--------------------------#
    
    dbc.Row([
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
                                    className="col-md-6",
                                ),
                                dbc.Col(
                                    dbc.CardBody(
                                        [
                                            html.H4("Notre Solution", className="card-title text-center p-4"),
                                            html.P(
                                                "Notre solution repose sur un modèle de prédiction avancé, conçu pour identifier les risques de maladies chroniques avec une précision inégalée. En combinant des algorithmes d'intelligence artificielle avec des données cliniques actualisées, nous offrons un dépistage personnalisé qui tient compte de l'historique médical et des habitudes de vie de chaque individu. Grâce à notre plate-forme intuitive, vous pouvez réaliser un dépistage complet en quelques clics pour mieux prévenir les complications. Ensemble, transformons la prévention et faisons de la santé une priorité accessible à tous",                                                className="card-text",
                                            )
                                        ]
                                    ),
                                    className="col-md-6",
                                ),
                            ],
                            className="bg-warning bg-opacity-50 text-black g-0 d-flex align-items-center text-center",
                        )
                    ],
    className="mb-3",
    ),
    width= {"size":11,"offset":0}),
    ]),
    
    dbc.Row(style={"height": "5vh"}),
    
    #------------------------Nos valeurs--------------------------#
    
    dbc.Row([
        dbc.Col(
                dbc.Card(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.CardBody(
                                        [
                                            html.H4("Nos valeurs", className="card-title text-center p-2"),
                                            html.P(
                                                "PRÉCISION : Chaque diagnostic est basé sur des données cliniques rigoureusement validées par des experts.",
                                                className="card-text"
                                                ),
                                            html.P(
                                                "INNOVATION : Nous sommes constamment à la recherche de nouvelles méthodes pour améliorer nos technologies et offrir des solutions toujours plus performantes."
                                                ,className="card-text"
                                                ),
                                            html.P(
                                                "CONFIDENTIALITÉ : Nous avons à coeur de respecter le secret médical. Les informations que vous saisissez ne sont ni enregistrées ni envoyées, elles ne quitteront jamais votre ordinateur."
                                                ,className="card-text"
                                                ),
                                            html.P(
                                                "ACCESSIBILITÉ : Notre outil est intuitif, simple et rapide d'utilisation."
                                                ,className="card-text"
                                                )

                                        ]
                                    ),
                                    className="col-md-6",
                                ),
                                
                                dbc.Col(
                                    dbc.CardImg(
                                        src=r"\assets\images\cinq-valeurs.jpg",
                                        className="img-fluid rounded-start",
                                    ),
                                    className="col-md-6",
                                )
                            ],
                            className="bg-primary text-white g-0 d-flex align-items-center  text-center",
                        )
                    ],
    className="mb-3",
    ),
    width= {"size":11,"offset":1}),
    ]),
    dbc.Row(style={"height": "5vh"}),
    
    #------------------------Avis--------------------------#

    dbc.Row([
                dbc.Col(width = 3),
                dbc.Col(html.H2("Ils témoignent",
                                className="bg-light text-black p-4 text-center"),
                        width = 6)
    ]),

    dbc.Row([
                dbc.Col(width = 3),
                dbc.Col(dbc.Carousel(
                            items=[
                                {"key": "1", "src": r"/assets\images\dr_group.png"},
                                {"key": "2", "src": r"/assets\images\dr_soucis.png"},
                                {"key": "3", "src": r"/assets\images\dr_GPT.png"},
                                {"key": "4", "src": r"\assets\images\Dr_chat.png"},
                            ],
                            controls=True,
                            indicators=True,
                            interval=3000
                            ),
                        width = 6)
            ])
])