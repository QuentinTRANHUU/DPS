from dash import register_page, callback, Input, Output, State, html, ALL
import generique_page_maladie
import pandas as pd


# Enregistrement de la page
register_page(__name__)

df_relative_path = r"\dataframes\clean_ckd_df.csv"

page_name = "Maladie Rénale Chronique"

image_page = r"\assets\images\maladie_reinale.jpeg"

col_name = {"Maladie Rénale Chronique": {"age" : "Age",
                                        "bp" : "Pression arterielle",
                                        "sg" : "Gravité spécifique",
                                        "al" : "Albumine (taux sanguin)",
                                        "su" : "Glycémie",
                                        "rbc" : "Globules rouges (nombre)",
                                        "pc" : "Globules blancs",
                                        "pcc" : "Présence d'aggrégats de globules blancs",
                                        "ba" : "Présence de bactéries",
                                        "bgr" : "Glycémie aléatoire",
                                        "bu" : "Urée sanguine",
                                        "sc" : "Creatinine sanguine",
                                        "sod" : "Sodium",
                                        "pot" : "Potassium",
                                        "hemo" : "Taux d'hémoglobine",
                                        "pcv" : "Volume globulaire moyen",
                                        "wc" : "Globule blancs (nombre)",
                                        "rc" : "Globule rouges (nombre)",
                                        "htn" : "Présence d'hypertension",
                                        "dm" : "Présence de diabete sucré",
                                        "cad" : "Présence de maladies cardiaques",
                                        "appet" : "Niveaux d'appétit",
                                        "pe" : "Présence d'oedème aux pieds",
                                        "ane" : "Présence d'anémie",
                                        "classification" : {"notckd": "Sain", "ckd":"Maladie Chronique des reins"}
    }}
    
# Créez la mise en page
df, model, score, layout = generique_page_maladie.create_layout(df_relative_path, page_name, col_name, image_page)

@callback(
    Output(page_name+'_resultat','children'),
    Input(page_name+'_submit_button','n_clicks'),
    State({"type": page_name+"_form_input", "index": ALL}, "value"),
    prevent_initial_call = True
)
def get_results(input,states):
    df_test = pd.DataFrame([states], columns=df.iloc[:,:-1].columns)
    
    result = col_name[page_name]["classification"][model.predict(df_test)[0]]
    
    return html.H4(f'{result} (probabilité de {model.predict_proba(df_test)[0][1 if result == "Sain" else 0] * 100 :.2f}%)', className='card-title text-center p-4')