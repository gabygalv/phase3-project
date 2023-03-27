from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.org import sessionmaker

#connected with db
engine = create_engine('sqlite:///encounter_counter.db', echo=True)

#manages tables
base = declarative_base()

#truther, ufo, sightings

class Truther(base):
    __tablename__ = 'truthers'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    base_location = Column(String)

    def __init__(self, id, username, base_location):
        self.id = id
        self.username = username
        self.base_location = base_location

class UFO(base):
    __tablename__ = 'UFOs'

    id = Column(Integer, primary_key=True)
    shape = Column(String)

    def __init__(self, id, shape='Unknown'):
        self.id = id
        self.shape = shape

class Sighting(base):
    __tablename__ = 'Sightings'

    id = Column(Integer, primary_key=True)
    location = Column(String)
    time = Column(DateTime)
    date = Column(DateTime)
    duration = Column(Integer)
    encounter_type = Column(String)
    summary = Column(String)
    truther_id = Column(Integer, ForeignKey('truthers.id'))
    ufo_shape = Column(String, ForeignKey('ufos.shape'))

    def __init__(self, id, location, time, date, duration, encounter_type, summary, truther_id, ufo_shape):
        self.id = id
        self.location = location
        self.time = time
        self.date = date
        self.duration = duration
        self.encounter_type = encounter_type
        self.summary = summary
        self.truther_id = truther_id
        self.ufo_shape = ufo_shape




    