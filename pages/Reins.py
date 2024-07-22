from dash import register_page
import generique_page_maladie


# Enregistrement de la page
register_page(__name__)

df_relative_path = r"\dataframes\clean_ckd_df.csv"

# Créez la mise en page
layout = generique_page_maladie.create_layout(df_relative_path, "Maladie Rénale Chronique")