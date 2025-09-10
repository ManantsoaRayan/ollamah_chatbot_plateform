import enum
from ..extensions import db
from .SessionModel import Session

class RoleEnum(enum.Enum):
    user = "user",
    system = "system"

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    role = db.Column(db.Enum(RoleEnum), nullable=False)
    content = db.Column(db.Text, nullable=False)
    
    session_id = db.Column(db.Integer, db.ForeignKey("session.id"), nullable=False)

    session = db.relationship(Session, backref="session")
