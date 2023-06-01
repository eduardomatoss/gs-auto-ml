from flask import Blueprint
from flask import request
from flask import render_template
from pycaret.regression import load_model
import pandas as pd


mod = Blueprint("predict", __name__)


@mod.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        df_predict = pd.DataFrame(
            {
                "Especie": [request.form.get("especie")],
                "Categoria": [request.form.get("categoria")],
                "Cultivar": [request.form.get("cultivar")],
                "Municipio": [request.form.get("municipio")],
                "UF": [request.form.get("uf")],
                "Dia_Plantio": [request.form.get("diaPlantio")],
                "Mes_Plantio": [request.form.get("mesPlantio")],
                "Ano_Plantio": [request.form.get("anoPlantio")],
                "Area": [request.form.get("area")],
            }
        )

        model = load_model("./model/pickle_lightgbm_pycaret")
        predict_result = model.predict(df_predict)
        predict_result = "%.2f" % predict_result

        return render_template("predict.html", result=predict_result)
    return render_template("predict.html", result=None)
