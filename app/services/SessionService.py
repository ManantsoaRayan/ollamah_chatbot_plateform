from ..extensions import db
from ..models import Session

class SessionService:
    """
        Session service
    """
    current_session = None

    @staticmethod
    def createSession(session_name):
        session = Session(name = session_name)
        db.session.add(session )
        db.session.commit()
        SessionService.current_session = session   
        return session
    
    @staticmethod
    def all():

        return Session.query.all()

    