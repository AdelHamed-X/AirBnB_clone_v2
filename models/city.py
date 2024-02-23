#!/usr/bin/python3
"""This is the city class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    if models.storage_type == 'db':
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities')
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """ Initialising objects with inherited adjectives """
        super().__init__(*args, **kwargs)