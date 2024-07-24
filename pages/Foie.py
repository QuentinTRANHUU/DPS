from dash import register_page, callback, Input, Output, State, html, ALL
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
                                "Dataset": {2: "Sain", 1: "Maladie Chronique du foie"}}
                }
    
# Créez la mise en page
df, model, layout = generique_page_maladie.create_layout(df_relative_path, page_name, col_name)

@callback(
    Output(page_name+'_resultat','children'),
    Input(page_name+'_submit_button','n_clicks'),
    State({"type": page_name+"_form_input", "index": ALL}, "value"),
    prevent_initial_call = True
)
def get_results(input,states):
    df_test = pd.DataFrame([states], columns=df.iloc[:,:-1].columns)
    
    return html.H4(f'{model.predict(df_test)[0]}', className='card-title text-center p-4')