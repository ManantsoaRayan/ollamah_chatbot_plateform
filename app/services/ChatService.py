from ollama import chat

class Chat_Service:
    """
        Chat services
    """
    @staticmethod
    def stream_response(prompt: str):
        return chat(
            model="llama3.1:8b",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
    
    