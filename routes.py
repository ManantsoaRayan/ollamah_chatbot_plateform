from flask import Blueprint, render_template, jsonify, request

routes = Blueprint("routes", __name__, static_folder="static")

def fetch_ollama_chat(message: str):
    pass

@routes.route("/")
def home(user:str = "rayan"):
    return render_template("index.html", user = user)

@routes.route("/api/generate", methods=["POST"])
def api():

    if request.method != "POST":
        return jsonify({"error 304": "Wrong Method"})
    
    message = request.form["message"]

    data = fetch_ollama_chat(message)

    return jsonify({"message": "Api endpoint"})