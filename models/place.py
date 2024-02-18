#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer, Float, Table
from sqlalchemy import MetaData
from sqlalchemy.orm import relationship
from os import environ
import models
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    if environ.get("HBNB_TYPE_STORAGE") == 'db':
        reviews = relationship('Review', cascade='all, delete, delete-orphan',
                           backref='place')
    else:
        @property
        def reviews(self):
            """ Getter method """
            all_reviews = models.storage.all(Review)
            places_list = []
            for review in all_reviews.values():
                if (review.place_id == self.id):
                    places_list.append(review)
            return (places_list)
    
    metadata = MetaData()
    place_amenity = Table('place_amenity', metadata,
                          Column('place_id', String(60),
                          ForeignKey('places.id'), primary_key=True,
                          nullable=False),
                          Column('amenity_id', String(60),
                          ForeignKey('amenities.id'), primary_key=True,
                          nullable=False))
