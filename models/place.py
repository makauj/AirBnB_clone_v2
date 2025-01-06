#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, ForeignKey
from sqlalchemy import String, Column,Integer, Float
from sqlalchemy.orm import relationship
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place', cascade='delete')
    amenities = relationship('Amenity', secondary='place_amenity',
                             viewonly=False)
    amenity_ids = []
    
    if getenv('HBNB_TYPE_STORAGE', None) != 'db':
        @property
        def reviews(self):
            """List all linked reviews"""
            review_list =[]
            for review in list(models.storage.all(Review).values()):
                if review.places_id == self.id:
                    review_list.append(review)
            return review_list
        
        @property
        def amenities(self):
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list
        
        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
