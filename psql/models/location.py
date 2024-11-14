from sqlalchemy import Column, Integer, Date, String, ForeignKey, Float
from psql.psql_functions import Base
from sqlalchemy.orm import relationship


class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, autoincrement=True)
    lat = Column(Float)
    lon = Column(Float)
    city = Column(String)
    country = Column(String)

    __table_args__ = (
        UniqueConstraint('lat', 'lon', 'city', 'country', name='uq_location'),
    )


    email = relationship("Email", back_populates="location", cascade="all, delete-orphan")