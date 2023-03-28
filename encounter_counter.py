import click

from lib.db.models import Truther, UFO, Sighting
from lib.helpers import main_menu, report_sighting

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///encounter_counter.db')
session = sessionmaker(bind=engine)

def encounter_counter():
    main_menu()    

    print("Thank you for using Encounter Counter!")

