from ..extensions import db
from sqlalchemy import DateTime
from datetime import datetime

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    created_at = db.Column(DateTime, default=datetime.now)

    def __init__(self, name:str) -> None:
        super().__init__()
        self.name = name

