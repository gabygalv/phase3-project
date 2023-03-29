from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, DateTime, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base

#manages tables
Base = declarative_base()

#truther, ufo, sightings
class Truther(Base):
    __tablename__ = 'truthers'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    username = Column(String())
    base_location = Column(String())

    def __repr__(self):
     return f"ID: {self.id}, " \
            + f"Username: {self.username}, " \
            + f"Base Location: {self.base_location}, " \

class UFO(Base):
    __tablename__ = 'ufos'
    __table_args__ = (PrimaryKeyConstraint('id'),)


    id = Column(Integer())
    shape = Column(String())

    def __repr__(self):
     return f"ID: {self.id}," \
            + f"Shape: {self.shape}," \


class Sighting(Base):
    __tablename__ = 'sightings'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    location = Column(String())
    time = Column(String()) #changed DateTime to String
    date = Column(String()) # """"""""""""""
    duration = Column(Integer())
    encounter_type = Column(String())
    summary = Column(String())
    # truther_id = Column(Integer, ForeignKey('truthers.id'))
    ufo_shape = Column(String, ForeignKey('ufos.shape'))

    def __repr__(self):
     return f"ID: {self.id}, " \
            + f"Location: {self.location}, " \
            + f"Time: {self.time}, " \
            + f"Date: {self.date}, " \
            + f"Duration: {self.duration}, " \
            + f"Encounter Type: {self.encounter_type}, " \
            + f"Summary: {self.summary}, " \
            + f"UFO Shape: {self.ufo_shape}, " \


# + f"Truther ID: {self.truther_id}, " \
    