from flask import Blueprint, Flask, render_template
from .api_route import api_bp
from .session_route import session_bp

routes = Blueprint("routes", __name__, static_folder="static")

@routes.route("/")
def home(user:str = "rayan"):
    return render_template("index.html", user = user)

def register_blueprints(app: Flask):
    app.register_blueprint(routes)
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(session_bp, url_prefix="/session")

