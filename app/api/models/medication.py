from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


from app.db import Base


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
