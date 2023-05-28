import io
import base64

from flask import Blueprint
from flask import render_template
import matplotlib.pyplot as plt

mod = Blueprint("example", __name__)


@mod.route("/", methods=["GET", "POST"])
def example():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    fig, ax = plt.subplots()
    ax.plot(x, y)

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode("utf-8")

    return render_template("example.html", image_base64=image_base64)
