from dash import register_page, callback, Input, Output, State, html, ALL
import generique_page_maladie
import pandas as pd

# Enregistrement de la page
register_page(__name__)

df_relative_path = r"\dataframes\diabete_clean.csv"

page_name = "Diabète"

col_name = {"Diabète": {"Pregnancies": "Nombre de Grossesses",
                        "Glucose": "Glucose",
                        "BloodPressure": "Pression Sanguine",
                        "Insulin": "Insuline",
                        "BMI": "Indice de Masse Corporel",
                        "DiabetesPedigreeFunction": "Fonction d'hérédité",
                        "Age": "Age",
                        "Outcome": {0: "Absence de diabète", 1: "Présence de diabète"}}
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