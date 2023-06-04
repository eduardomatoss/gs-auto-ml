from pycaret.regression import load_model
import pandas as pd
import streamlit as st

model = load_model("./model/pickle_lightgbm_pycaret")


def page():
    with st.form("form"):
        df_predict = {}

        df_predict["Especie"] = st.text_input("Especie")
        df_predict["Categoria"] = st.multiselect(
            "Categoria", ["Genetica", "Basica", "C1", "C2", "S1", "S2"]
        )
        df_predict["Cultivar"] = st.text_input("Cultivar")
        df_predict["Municipio"] = st.text_input("Municipio")
        df_predict["UF"] = st.text_input("UF")
        df_predict["Dia_Plantio"] = st.number_input("Dia Plantio")
        df_predict["Mes_Plantio"] = st.number_input("Mes Plantio")
        df_predict["Ano_Plantio"] = st.number_input("Ano Plantio")
        df_predict["Area"] = st.number_input("Area")

        submitted = st.form_submit_button("Estimar")
        if submitted:
            valid_data = [data for data in df_predict.values() if data]

            if not valid_data:
                return st.error("Valores invalidos, por favor revisar")

            df = pd.DataFrame(df_predict)
            predict_result = model.predict(df)
            predict_result = "%.2f" % predict_result
            return st.success(f"Producao Estimada: {predict_result}")
