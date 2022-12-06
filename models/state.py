#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import relationship
from models.city import City
import models
import shlex


class State(BaseModel, Base):
    """Defines State class that inherits from BaseModel and Base classes"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        h_city = models.storage.all()
        list_a = []
        list_b = []
        for k in h_city:
            city = k.replace(".", " ")
            city = shlex.split(city)
            if city[0] == "City":
                list_a.append(h_city[k])
        for element in list_a:
            if element.state_id == self.id:
                list_b.append(element)
        return list_b
