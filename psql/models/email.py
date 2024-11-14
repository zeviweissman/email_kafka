from sqlalchemy import Column, Integer, Date, String, ForeignKey
from psql.psql_functions import Base
from sqlalchemy.orm import relationship


class Email(Base):
    __tablename__ = "email"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String)
    username = Column(String)
    ip_address = Column(String)
    email_date = Column(Date)
    device_id = Column(Integer, ForeignKey("device.id"))
    location_id = Column(Integer, ForeignKey("location.id"))

    device = relationship("Device", back_populates="email", lazy='joined')
    location = relationship("Location", back_populates="email", lazy='joined')
    sentences = relationship("Sentence", back_populates="email", lazy='joined', cascade="all, delete-orphan")