
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Truther, UFO, Sighting
from helpers import create_table, create_sighting, create_truther, login

import click
# from lib.x_cli import tacos

#connect with db
engine = create_engine('sqlite:///encounter_counter.db')
session = sessionmaker(bind=engine)


@click.command()
@click.option('--func', '-f', help="Runs the requested function", required=True, 
    prompt='''
    ______                             __               ______                  __           
   / ____/___  _________  __  ______  / /____  _____   / ____/___  __  ______  / /____  _____
  / __/ / __ \/ ___/ __ \/ / / / __ \/ __/ _ \/ ___/  / /   / __ \/ / / / __ \/ __/ _ \/ ___/
 / /___/ / / / /__/ /_/ / /_/ / / / / /_/  __/ /     / /___/ /_/ / /_/ / / / / /_/  __/ /    
/_____/_/ /_/\___/\____/\__,_/_/ /_/\__/\___/_/      \____/\____/\__,_/_/ /_/\__/\___/_/
    [report] :   Report a UFO sighting.
        ------------------------------------------
    [profile]:   See profile menu.
        ------------------------------------------
    [login]  :   Login to Encounter Counter.
        ------------------------------------------
    Enter the function you would like to execute: ''')

def encounter_counter(func, name = "Jayson"):
    if func == 'report':
        tacos(name)
    else:
        print("Invalid Operation")
    pass 