from psql.models import HostageSentence, ExplosiveSentence, Email
from psql.psql_functions import get_session
from sqlalchemy.orm import load_only


def get_all_sentences():
    with get_session() as session:
            return session.query(HostageSentence).all() + session.query(ExplosiveSentence).all()

