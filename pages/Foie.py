from dash import register_page, callback, Input, Output, State, html, ALL
import dash_bootstrap_components as dbc
import generique_page_maladie
import pandas as pd


# Enregistrement de la page
register_page(__name__)

df_relative_path = r"\dataframes\liver_cleaned.csv"

page_name = "Maladies du Foie"

col_name = {"Maladies du Foie": {"Age": "Age",
                                "Gender": "Genre",
                                "Total_Bilirubin": "Bilirubine Totale",
                                "Alkaline_Phosphotase": "Alkaline Phosphotase",
                                "Alamine_Aminotransferase": "Alamine Aminotransferase",
                                "Albumin_and_Globulin_Ratio": "Taux d'Albumine sur Globuline",
                                "Dataset": {0: "Sain", 1: "Maladie Chronique du foie"}}
                }
    
# Créez la mise en page
df, model, score, precision, falseNeg, layout = generique_page_maladie.create_layout(df_relative_path, page_name, col_name)

@callback(
    Output(page_name+'_resultat','children'),
    Input(page_name+'_submit_button','n_clicks'),
    State({"type": page_name+"_form_input", "index": ALL}, "value"),
    prevent_initial_call = True
)
def get_results(input,states):
    df_test = pd.DataFrame([states], columns=df.iloc[:,:-1].columns)
    
    result = col_name[page_name]["Dataset"][model.predict(df_test)[0]]
    
    return html.H4(f'{result} (probabilité de {model.predict_proba(df_test)[0][0 if result == "Sain" else 1] * 100 :.2f}%)', className='card-title text-center p-4'), \
        dbc.Accordion(
            [dbc.AccordionItem(
                [html.P(f'Accuracy score de {score * 100 :.2f}%', className='card-title text-center text-white '),
                 html.P(f'Précision de {precision * 100 :.2f}%', className='card-title text-center text-white'),
                 html.P(f'Taux de faux négatifs de {falseNeg * 100 :.2f}%', className='card-title text-center text-white')],
                title = "Statistiques du test",
                className = 'card-title text-center bg-primary')],
            start_collapsed = True,
            className='card-title text-center bg-secondary')
