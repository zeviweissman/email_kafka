from typing import List

from psql.models import Email
from psql.psql_functions import get_session
from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError


def insert_email(email: Email) -> Result[Email, str]:
    with get_session() as session:
        try:
            session.add(email)
            session.commit()
            session.refresh(email)
            return Success(email)
        except SQLAlchemyError as e:
            return Failure(e)



def get_emails_by_email_address(email_address) -> List[Email]:
    with get_session() as session:
            return session.query(Email).filter_by(email_address = email_address).all()
