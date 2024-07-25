from dash import Dash, html,page_container, callback, Input, Output
import dash_core_components as dcc
import dash_bootstrap_components as dbc

# Création de l'application Dash
app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB], use_pages=True)
app.title = 'DPS'
app._favicon = (r"\assets\favicon.ico")


# Créez la mise en page
app.layout = dbc.Container(
    [
        dcc.Location(id='url'),
        dbc.Row(className="g-0 gy-1"),

        #------------------------Nav Bar--------------------------#
        
        dbc.Nav(
            [
                dbc.Stack([
                        html.A(
                            href= "/accueil",
                            children=[html.Img(src = r"\assets\images\Logo.png", height="70px")],
                            className="ms-4 m-2"
                            ),
                        dbc.NavItem
                            ([
                                dbc.Row([html.H1("La Data au service de la Santé", className = "text-white text-center mt-1 fs-1")]),
                                html.Hr(style={"color":"white"},className="m-0 mb-1"),
                                dbc.Row([html.H4("", className = "text-white text-center", id = "Nav_nom_page")])
                            ],
                            className="mx-auto"),
                        dbc.NavItem(dbc.NavLink("Informations", href="/informations",className="text-white fs-4")),
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
                            className="text-light me-4 fs-4"
                            )
                        ],
                        direction="horizontal",
                        gap=3)
            ],
            className = "bg-primary position-fixed top-0 w-100 border-bottom border-white"
        ),
        
        #------------------------Content--------------------------#
    
        page_container,
        dbc.Row(className="g-0 gy-2"),
    
        #------------------------footer--------------------------#

        dbc.Row(
            [
                #colonne vide pour corriger l'alignement
                dbc.Col(
                    [dbc.Row(html.P("Powered by Vivi Data Consulting, with love ❤️", className = "text-white ms-4", style = {"font-style": "italic"}))],
                    align = "end",
                    width=10),
                
                # Logo
                dbc.Col(html.Img(src = r"\assets\images\WCS_logo.png",
                                className="img-rounded bg-primary h-100 ms-5"),
                        style={"height": "60px"}
                        )
            ],
        # background du header
        className="bg-primary g-0 position-fixed bottom-0 w-100 border-top border-white")
    ],
    fluid=True,
    class_name="lh-lg g-0  font-Garamond")

#nom de page dynamique
@callback(
    Output('Nav_nom_page', 'children'),
    Input('url', 'pathname')
    )
def set_nav_name_page(p_name):
    dico = {"/diabete":"Diabète",
            "/foie" : "Maladies du foie",
            "/reins" : "Maladie rénale chronique",
            "/coeur" : "Maladies cardiaques",
            "/accueil":"Accueil",
            "/informations" : "Informations"}
    return dico[p_name]

# Lancez l'application
if __name__ == '__main__':
    app.run_server(debug=True)