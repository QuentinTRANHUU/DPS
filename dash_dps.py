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
    
        # dbc.Row(
        #     [
        #         # Logo
        #         dbc.Col(html.Img(src = r"\assets\images\Logo.png",
        #                         className="img-rounded bg-primary h-100"),
        #                 style={"height": "15vh"}
        #                 ),
                
        #         # Devise
        #         dbc.Col(html.H1('La Data au service de la Santé.',
        #                         className="bg-primary text-white p-4 text-center h-100"),
        #                 style={"height": "15vh"}
        #                 ),
        #         #colonne vide pour corriger l'alignement
        #         dbc.Col()
        #     ],
        # # background du header
        # className="bg-primary"),

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
                    dbc.NavItem(dbc.NavLink("Informations", href="/informations")),
                    dbc.DropdownMenu(
                        children=[
                            dbc.DropdownMenuItem("Diabète", href = "/diabete"),
                            dbc.DropdownMenuItem("Maladies du foie", href = "/foie"),
                            dbc.DropdownMenuItem("Maladie rénale chronique", href = "/reins"),
                            dbc.DropdownMenuItem("Maladies cardiaques", href = "/coeur"),
                        ],
                        nav=True,
                        in_navbar=True,
                        menu_variant="dark",
                        direction="start",
                        label="Tests",
                    ),
                ],
                brand = dbc.Row(
                                [
                                    dbc.Col(html.Img(src = r"\assets\images\Logo.png", height="60px")),
                                    dbc.Col(dbc.NavbarBrand("Accueil")),
                                    # dbc.Col(dbc.NavbarBrand("  ")),
                                    # dbc.Col(dbc.NavbarBrand("  ")),
                                    # dbc.Col(dbc.NavbarBrand("  ")),
                                    # dbc.Col(dbc.NavbarBrand("  ")),
                                    # dbc.Col(dbc.NavbarBrand("  ")),
                                    # dbc.Col(dbc.NavbarBrand("  ")),
                                    # dbc.Col(dbc.NavbarBrand("  ")),
                                    # dbc.Col(dbc.NavbarBrand("La Data au service de la Santé")),
                                ],
                                align="center",
                                # className="g-0",
                            ),
                brand_href="/accueil",
                color="primary",
                dark=True,
                sticky = "top",
                style = {"align-items": "center"}
            ),
            
        # dbc.Row([
        #     dbc.ButtonGroup(
        #         [
        #             dbc.Button("Accueil", outline=True, color="dark", href = "/accueil",className="bg-light"),
        #             dbc.Button("Diabète", outline=True, color="dark", href = "/diabete",className="bg-light"),
        #             dbc.Button("Maladies du foie", outline=True, color="dark", href = "/foie",className="bg-light"),
        #             dbc.Button("Maladie rénale chronique", outline=True, color="dark", href = "/reins",className="bg-light"),
        #             dbc.Button("Maladies cardiaque", outline=True, color="dark", href = "/coeur",className="bg-light"),
        #             dbc.Button("Informations", outline=True, color="dark", href = "/informations",className="bg-light"),
        #         ])
        # ],
        # # background de la Nav Bar
        # className="bg-primary"),
        
        # # espace sous la nav bar
        # dbc.Row(style={"height": "1vh"}),
    
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