from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Truther, UFO, Sighting
from helpers import create_table, create_sighting, create_truther, login

import click
# from lib.x_cli import tacos

#connect with db
engine = create_engine('sqlite:///encounter_counter.db')
session = sessionmaker(bind=engine)

import click
from lib.helpers import main_menu, report

def encounter_counter():
    main_menu()    

    print("Thank you for using Encounter Counter!")
