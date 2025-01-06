#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename = 'states'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Return list of city instances related to state"""
            from models import storage
            list_cities = []
            for city in storage.all(City).value(s):
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
