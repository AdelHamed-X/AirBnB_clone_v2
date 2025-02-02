#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import environ
import models
from models.review import Review
from models.city import City

if environ.get("HBNB_TYPE_STORAGE") == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                            Column('place_id', String(60),
                            ForeignKey('places.id'), primary_key=True,
                            nullable=False),
                            Column('amenity_id', String(60),
                            ForeignKey('amenities.id'), primary_key=True,
                            nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_type == 'db':
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
        reviews = relationship('Review', backref='place')
        amenities = relationship('Amenity', secondary="place_amenity",
                                    backref="place_amenities",
                                    viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Getter method """
            all_reviews = models.storage.all(Review)
            places_list = []
            for review in all_reviews.values():
                if (review.place_id == self.id):
                    places_list.append(review)
            return (places_list)
        
        @property
        def amenities(self):
            """getter attribute returns the list of Amenity instances"""
            from models.amenity import Amenity
            amenity_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list
