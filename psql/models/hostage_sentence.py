from sqlalchemy import Column, Integer, String, ForeignKey
from psql.psql_functions import Base
from sqlalchemy.orm import relationship


class HostageSentence(Base):
    __tablename__ = "hostage_sentence"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(String)
    email_id = Column(Integer, ForeignKey("email.id"))

    email = relationship("Email", back_populates="hostage_sentences", lazy='joined')