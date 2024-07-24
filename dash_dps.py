from dash import Dash, html,page_container
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Création de l'application Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB], use_pages=True)
app.title = 'DPS'
app._favicon = (r"\assets\favicon.ico")


# Créez la mise en page
app.layout = dbc.Container(
    [

    #------------------------Nav Bar--------------------------#
            dbc.NavbarSimple(
                children=[
                    dbc.NavItem(dbc.Row(
                                [
                                    dbc.Col(html.H3("La Data au service de la Santé", className = "text-white text-center"), width={"size" : "auto"}),
                                    dbc.Col(html.H3("   ")),
                                    dbc.Col(html.H3("   ")),
                                    dbc.Col(html.H3("   ")),
                                    dbc.Col(html.H3("   ")),
                                    dbc.Col(html.H3("   ")),
                                    dbc.Col(html.H3("   ")),
                                    dbc.Col(html.H3("   ")),
                                    dbc.Col(html.H3("   ")),
                                    dbc.Col(html.H3("   ")),
                                    dbc.Col(html.H3("   ")),
                                    dbc.Col(html.H3("   "), width = 3)
                    ], align = "center")),
                    dbc.NavItem(dbc.NavLink("Informations", href="/informations",className="text-white")),
                    dbc.DropdownMenu(
                        children=[
                            dbc.DropdownMenuItem("Diabète", href = "/diabete",className="text-black"),
                            dbc.DropdownMenuItem("Maladies du foie", href = "/foie",className="text-black"),
                            dbc.DropdownMenuItem("Maladie rénale chronique", href = "/reins",className="text-black"),
                            dbc.DropdownMenuItem("Maladies cardiaques", href = "/coeur",className="text-black"),
                        ],
                        nav = True,
                        in_navbar = True,
                        align_end = True,
                        label = "Tests",
                        className="text-light"
                    ),
                ],
                brand = dbc.Row(
                                [
                                    dbc.Col(html.Img(src = r"\assets\images\Logo.png", height="60px")),
                                    dbc.Col(dbc.NavbarBrand("Accueil")),
                                ],
                                align="center",
                            ),
                brand_href="/accueil",
                color="primary",
                dark=True,
                sticky = "top",
                style = {"align-items": "center"}
            ),

    
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