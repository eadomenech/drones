from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_imageattach.entity import Image, image_attachment

from ...db import Base


class MedicationModel(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    weight = Column(Float)
    code = Column(String, index=True)
    image = image_attachment('MedicationPictureModel')


class MedicationPictureModel(Base, Image):
    """Medication picture model."""
    __tablename__ = 'medication_pictures'

    medication_id = Column(
        Integer, ForeignKey('medications.id'), primary_key=True)
    medication = relationship('MedicationModel')

