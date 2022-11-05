from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy import Enum
from sqlalchemy.orm import relationship

from app.db import Base
from app.api.enums import DroneEnumModel, DroneEnumState


class DroneModel(Base):
    __tablename__ = "drones"

    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String(100), unique=True, index=True)
    model = Column(Enum(DroneEnumModel), default=DroneEnumModel.Lightweight)
    weight_limit = Column(Float)
    battery_capacity = Column(Integer)
    state = Column(Enum(DroneEnumState), default=DroneEnumState.IDLE)

    medications = relationship(
        "MedicationModel", back_populates="drone")

    def __repr__(self):
        return f'Drone(serial_number={self.serial_number})'


class MedicationModel(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    weight = Column(Float)
    code = Column(String, index=True)
    image = Column(String)
    drone_id = Column(Integer, ForeignKey("drones.id"))

    drone = relationship("DroneModel", back_populates="medications")

    def __repr__(self):
        return f'Medication(name={self.name})'
