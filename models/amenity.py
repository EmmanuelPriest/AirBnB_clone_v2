#!/usr/bin/python3

"""Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from os import getenv


class Amenity(BaseModel, Base):
    """class Amenity that inherits from BaseModel and Base classes"""
    __tablename__ = "amenities"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
