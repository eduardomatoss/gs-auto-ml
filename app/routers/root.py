from flask import Blueprint
from flask import render_template


mod = Blueprint("main", __name__)


@mod.route("/")
def root():
    return render_template("index.html")
