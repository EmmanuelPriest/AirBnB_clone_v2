#!/usr/bin/python3

""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Sequence
from sqlalchemy.orm import relationship
from models.city import City
from models import storage_type
from os import getenv


class State(BaseModel, Base):
    """Defines State class that inherits from BaseModel and Base classes"""
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """Returns list of City objects with state_id = current State.id"""
        from models import storage
            rel_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    rel_cities.append(city)
            return rel_cities
