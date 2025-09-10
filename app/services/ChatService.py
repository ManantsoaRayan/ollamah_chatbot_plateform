from ollama import chat
from ..extensions import db

class Chat_Service:
    """
        Chat services
    """
    @staticmethod
    def stream_response(prompt: str):
        response=  chat(
            model="llama3.1:8b",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )

        return response
    
    