from flask import Blueprint, request, Response, stream_with_context
from ..services import Chat_Service
import json

api_bp = Blueprint("api", __name__)

@api_bp.route("/generate", methods=["GET"])
def chat_api() -> Response:
    
    prompt = request.args.get("prompt", "")

    def generate():

        # ollama stream
        stream = Chat_Service.stream_response(prompt)

        for chunk in stream:
            text = chunk["message"].get("content", "")
            if text:
                # send chunk as JSON line (SSE-like)
                yield f"data: {json.dumps(text)}\n\n"

        yield f"event: done\ndata: [DONE]\n\n"


    # Response with text/event-stream so browser can stream
    return Response(stream_with_context(generate()), content_type="text/event-stream")