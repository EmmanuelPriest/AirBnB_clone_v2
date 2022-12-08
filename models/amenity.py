#!/usr/bin/python3

"""Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """class Amenity that inherits from BaseModel and Base classes"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
