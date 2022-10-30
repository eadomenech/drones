from sqlalchemy import Column, Integer, String, Float
from sqlalchemy_utils.types.choice import ChoiceType

from ...db import Base


class DroneModel(Base):

    STATE_TYPES = [
        ('idle', 'IDLE'),
        ('loading', 'LOADING'),
        ('loaded', 'LOADED'),
        ('delivering', 'DELIVERING'),
        ('delivered', 'DELIVERED'),
        ('returning', 'RETURNING')
    ]

    MODEL_TYPES = [
        ('lightweight', 'Lightweight'),
        ('middleweight', 'Middleweight'),
        ('cruiserweight', 'Cruiserweight'),
        ('heavyweight', 'Heavyweight')
    ]

    __tablename__ = "drones"

    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String(100), unique=True, index=True)
    # model = Column(ChoiceType(MODEL_TYPES), unique=True)
    model = Column(String)
    weight_limit = Column(Float)
    battery_capacity = Column(Integer)
    # state = Column(ChoiceType(STATE_TYPES))
    state = Column(String)
