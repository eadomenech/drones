from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.choice import ChoiceType

from ..db import Base


class Drone(Base):
    STATE_TYPES = [
        ('idle', 'IDLE'),
        ('loading', 'LOADING'),
        ('loaded', 'LOADED'),
        ('delivering', 'DELIVERING'),
        ('delivered', 'DELIVERED'),
        ('returning', 'RETURNING')
    ]

    __tablename__ = "drones"

    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String(100), unique=True, index=True)
    model = Column(String, unique=True)
    weight_limit = Column(Float)
    battery_capacity = Column(Float)
    state = Column(ChoiceType(STATE_TYPES))


class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    weight = Column(Float)
    code = Column(String, index=True)
    image = Column(String)
