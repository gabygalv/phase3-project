from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer, DateTime, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from prettytable import PrettyTable

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
     return f"ID: {self.id}, \n" \
            + f"Shape: {self.shape}, \n" \
            +"***************** \n"


class Sighting(Base):
    __tablename__ = 'sightings'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    location = Column(String())
    time = Column(String())
    date = Column(String())
    duration = Column(Integer())
    encounter_type = Column(String())
    summary = Column(String())
    truther_id = Column(Integer, ForeignKey('truthers.id'))
    ufo_id = Column(Integer, ForeignKey('ufos.id'))

    truther = relationship('Truther', backref='truthers')
    ufo = relationship('UFO', backref='ufos')

    def get_data_tuple(self):
       return {
          'id': self.id,
          'location':self.location,
          'time': self.time,
          'date': self.date,
          'duration': self.duration,
          'encounter_type': self.encounter_type,
          'summary': self.summary,
          'truther': self.truther,
          'ufo': self.ufo
       }

    def build_encounter_table(self):

        x = PrettyTable()
        x.field_names = ("Encounter Report", "")
        x.align[""] = 'l'
        x.add_rows(
            [
                ["Location", self.location],
                ["Time", self.time],
                ["Date", self.date],
                ["Duration", self.duration],
                ["Encounter Type", self.encounter_type],
                ["Summary", self.summary],
                ["Truther", self.truther.username],
                ["UFO Shape", self.ufo.shape]
            ]
        )

        return(x)
        
    def __repr__(self):
     return f"Location: {self.location}, \n" \
            + f"Time: {self.time}, \n" \
            + f"Date: {self.date}, \n" \
            + f"Duration: {self.duration}, \n" \
            + f"Encounter Type: {self.encounter_type}, \n" \
            + f"Summary: {self.summary}, \n" \
            + "***************** \n"
            # + f"Truther ID: {self.truther_id}, \n" \
            # + f"UFO Shape ID: {self.ufo_id} \n" \





    