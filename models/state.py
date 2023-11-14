#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of state """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""
        cites = []

        @property
        def cities(self):
            city_list = []
            if models.storage_t != 'db':
                for city_object in models.storage.all(City).values():
                    if city_object.state_id == self.id:
                        city_list.append(city_object)
            return city_list