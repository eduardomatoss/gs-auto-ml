from os import path
from logging import getLogger

from flask import Flask
from waitress import serve

from app.routers.root import mod as root_router
from app.routers.predict import mod as predict_router
from app.common.log import create_logger

create_logger()
logger = getLogger()

template_dir = path.abspath("app/templates")
style_dir = path.abspath("app/static")

app = Flask(__name__, template_folder=template_dir, static_folder=style_dir)

app.register_blueprint(root_router, url_prefix="/")
app.register_blueprint(predict_router, url_prefix="/predict")

if __name__ == "__main__":
    logger.info("starting api")
    serve(app, host="0.0.0.0", port=5000)
