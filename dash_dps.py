from dash import Dash, html,page_container
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Création de l'application Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB], use_pages=True)


# Créez la mise en page
app.layout = dbc.Container(
    [
            
    #------------------------Header--------------------------#
    
        dbc.Row(
            [
                # Logo
                dbc.Col(html.Img(src = r"\assets\images\Logo.png",
                                className="img-rounded bg-primary h-100"),
                        style={"height": "15vh"}
                        ),
                
                # Devise
                dbc.Col(html.H1('La Data au service de la Santé.',
                                className="bg-primary text-white p-4 text-center h-100"),
                        style={"height": "15vh"}
                        ),
                #colonne vide pour corriger l'alignement
                dbc.Col()
            ],
        # background du header
        className="bg-primary"),

    #------------------------Nav Bar--------------------------#
    
        dbc.Row([
            dbc.ButtonGroup(
                [
                    dbc.Button("Accueil", outline=True, color="dark", href = "/accueil",className="bg-light"),
                    dbc.Button("Diabète", outline=True, color="dark", href = "/diabete",className="bg-light"),
                    dbc.Button("Maladies du foie", outline=True, color="dark", href = "/foie",className="bg-light"),
                    dbc.Button("Maladie rénale chronique", outline=True, color="dark", href = "/reins",className="bg-light"),
                    dbc.Button("Maladies cardiaque", outline=True, color="dark", href = "/coeur",className="bg-light"),
                    dbc.Button("Informations", outline=True, color="dark", href = "/informations",className="bg-light"),
                ])
        ],
        # background due la Nav Bar
        className="bg-primary"),
        
        #espace sous la nav bar
        dbc.Row(style={"height": "1vh"}),
    
    #------------------------Content--------------------------#
    
        page_container,
        
        dbc.Row(style={"height": "5vh"}),
    
    #------------------------footer--------------------------#

        dbc.Row(
            [
                #colonne vide pour corriger l'alignement
                dbc.Col(width=9),
                
                # Logo
                dbc.Col(html.Img(src = r"\assets\images\WCS_logo.png",
                                className="img-rounded bg-primary h-100"),
                        style={"height": "15vmin"},
                        width=3
                        )
            ],
        # background du header
        className="bg-primary")
    ])

# Lancez l'application
if __name__ == '__main__':
    app.run_server(debug=True)