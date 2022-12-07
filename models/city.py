#!/usr/bin/python3

""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from models import storage_type
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), nullable=False, ForeignKey("state.id"))
        places = relationship("Place", cascade="all, delete, delete-orphan",
                          backref="cities")
    else:
        name = ""
        state_id = ""
