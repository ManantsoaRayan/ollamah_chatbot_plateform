from flask import Blueprint, request, jsonify
from ..services import SessionService

session_bp = Blueprint("session", __name__)

@session_bp.route("/create", methods=["POST"])
def create():

    data = request.get_json() or {}
    session_name: str | None = data.get("session_name")

    if not session_name or session_name.strip() == "":
        return jsonify({"status": "failure", "error": "Session name required"})
    
    try:
        SessionService.createSession(session_name)
    except Exception as _:
        return jsonify({"status": "failure", "error": "Registration failed. Retry"})

    return jsonify({"status": "success", "session_name": session_name})

@session_bp.route("/all", methods=["POST"])
def all():

    data = SessionService.all()

    data = [{"id": session.id, "session_name": session.name} for session in data]

    return jsonify({"body": data})