from dash import Dash, html, dcc, Input, Output, State, callback
# from dash_dps import app
import numpy as np
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import formulaire

def create_layout(df_relative_path, page_name, col_name):

    from imblearn.over_sampling import RandomOverSampler
    from sklearn.ensemble import ExtraTreesClassifier, VotingClassifier, AdaBoostClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.linear_model import LogisticRegression, Perceptron
    from sklearn.neighbors import KNeighborsClassifier

    from sklearn.preprocessing import StandardScaler, OrdinalEncoder, PowerTransformer, TargetEncoder, OneHotEncoder
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import make_pipeline
    from sklearn.compose import ColumnTransformer

    df = formulaire.get_df(df_relative_path)
    
    # Dictionnaire qui va définir la pipeline en fonction de la maladie
    model_dict = {"Maladies du Foie": {"model": ExtraTreesClassifier(200),
                                       "scaler": PowerTransformer(),
                                       "encoder": OrdinalEncoder()},
                  "Maladies Cardiaques": {"model": VotingClassifier(estimators= [('LogisticRegression', LogisticRegression()), 
                                                                                 ('KNeighborsClassifier', KNeighborsClassifier()), 
                                                                                 ('Perceptron', Perceptron()), 
                                                                                 ('AdaBoostClassifier', AdaBoostClassifier())],
                                                                    voting = 'hard'),
                                       "scaler": StandardScaler(),
                                       "encoder": OneHotEncoder()},
                  "Diabète": {"model": ExtraTreesClassifier(200),
                                       "scaler": PowerTransformer(),
                                       "encoder": OrdinalEncoder()},
                  "Maladie Rénale Chronique": {"model": DecisionTreeClassifier(min_samples_split = 25,
                                                                                min_samples_leaf = 2,
                                                                                max_depth = 5,
                                                                                criterion= 'entropy',
                                                                                class_weight = 'balanced'),
                                             "scaler": StandardScaler(),
                                             "encoder": TargetEncoder()}}
    
    # Définition des types de colonnes:
    numeric_col = [column for column in df.iloc[:, :-1].select_dtypes(include=[np.number]).columns if df.iloc[:, :-1][column].nunique() > len(df.iloc[:, :-1])**(1/2)]
    cat_col = [column for column in df.iloc[:, :-1].columns if column not in numeric_col]
    
    # Définition de la pipeline
    pipeline = make_pipeline(
                            ColumnTransformer([
                                                ("numeric", model_dict[page_name]["scaler"], numeric_col),
                                                ("categoric", model_dict[page_name]["encoder"], cat_col)
                                                ]),
                            model_dict[page_name]["model"]
                                )
    
    # Définition du X et y
    X = df.iloc[:, :-1]
    y = df.iloc[:,-1:]

    if page_name == "Maladies du Foie":
        ros = RandomOverSampler(random_state=42)
        X, y = ros.fit_resample(X, y)
    
    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    # Train the model
    model = pipeline.fit(X_train, y_train)
    
    col_in_text = ""
    for col in df.iloc[:, :-1].columns:
        col_in_text += col_name[page_name][col] + ", "
    col_in_text = col_in_text[:-2] + "."
    
    # Créez la mise en page
    return df,model,dbc.Container([
        
        #------------------------Nom Page--------------------------#
        dbc.Row([
            dbc.Col(html.H1(page_name,
                            className="text-black p-4 text-center",
                            id = page_name+"_page_name"))
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
                                                    {col_in_text}",
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
                            formulaire.create_formulaire(df,page_name, col_name),
                            title=html.H4("Faites le Test", className="text-center"),
                                className="bg-light")
                        ],
                        start_collapsed=True
                        ),
                    className="mb-3",
                    width= 6)
        ])
    ])
    
    
#####################################################
# @callback(
#     Output('resultat','children'),
#     Input('submit_button','n_clicks'),
#     State('page_name','children'),
#     prevent_initial_call = True
# )
# def get_results(input,state):
#     return html.H4({df.columns}, className='card-title text-center p-4')
#######################################################