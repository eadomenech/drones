from sqlalchemy import Column, Integer, String, Float
from sqlalchemy_utils.types.choice import ChoiceType

from ...db import Base


class MedicationModel(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    weight = Column(Float)
    code = Column(String, index=True)
    image = Column(String)
