from flask import Blueprint, render_template, request, Response, stream_with_context
from ollama import chat
import json

routes = Blueprint("routes", __name__, static_folder="static")


@routes.route("/")
def home(user:str = "rayan"):
    return render_template("index.html", user = user)

@routes.route("/api/generate", methods=["GET"])
def api():
    
    prompt = request.args.get("prompt", "")

    def generate():
        # ollama stream

        stream = chat(
            model="llama3.1:8b",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )

        for chunk in stream:
            text = chunk["message"].get("content", "")
            if text:
                # send chunk as JSON line (SSE-like)
                yield f"data: {json.dumps(text)}\n\n"

        yield f"event: done\ndata: [DONE]\n\n"


    # Response with text/event-stream so browser can stream
    return Response(stream_with_context(generate()), content_type="text/event-stream")