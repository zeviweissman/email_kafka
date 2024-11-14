from sqlalchemy import Column, Integer, String, ForeignKey
from psql.psql_functions import Base
from sqlalchemy.orm import relationship


class Sentence(Base):
    __tablename__ = "sentence"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(str)
    email_id = Column(Integer, ForeignKey("email.id"))

    email = relationship("Email", back_populates="sentences", lazy='joined')