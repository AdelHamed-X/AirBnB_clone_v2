#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
from os import environ


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    if models.storage_type == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""
    
    def __init__(self, *args, **kwargs):
        """ Initialising objects with inherited adjectives """
        super().__init__(*args, **kwargs)

    if models.storage_type != 'db':
        @property
        def cities(self):
            all_cities = models.storage.all(City)
            city_list = []
            for elem in all_cities.values():
                if (elem.state_id == self.id):
                    city_list.append(elem)
            return (city_list)
