from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import Enum

from ...db import Base
from ..enums import DroneEnumModel, DroneEnumState


class DroneModel(Base):

    __tablename__ = "drones"

    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String(100), unique=True, index=True)
    model = Column(Enum(DroneEnumModel), default=DroneEnumModel.Lightweight)
    model = Column(String)
    weight_limit = Column(Float)
    battery_capacity = Column(Integer)
    state = Column(Enum(DroneEnumState), default=DroneEnumState.IDLE)
    state = Column(String)
