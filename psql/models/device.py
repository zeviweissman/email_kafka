from sqlalchemy import Column, Integer, Date, String, ForeignKey, Float, UniqueConstraint
from psql.psql_functions import Base
from sqlalchemy.orm import relationship




class Device(Base):
    __tablename__ = "device"
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String)
    browser = Column(String)
    os = Column(String)

    __table_args__ = (
        UniqueConstraint('device_id', 'browser', 'os', name='uq_device'),
    )

    email = relationship("Email", back_populates="device", cascade="all, delete-orphan")