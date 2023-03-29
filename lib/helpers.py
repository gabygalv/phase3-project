import click
from lib.db.models import (Sighting, Truther, Base)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///encounter_counter.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def main_menu ():

    choice = ""
    while choice != 'quit' and choice != 'q':
        print('''          
            [report  (r)]  : Report a UFO or UAP sighting. (requires login)
            [profile (p)]  : Create a profile/login. 
            [search  (s)]  : Search the Encounter Counter database.
            [quit    (q)]  : Exit Encounter Counter.
        ''')

        if (choice == 'r') or (choice == 'report'):
            report_sighting()
        if (choice == 'p') or (choice == 'profile'):
            profile()
        if (choice == 's') or (choice == 'search'):
            search()

        choice = click.prompt("Enter selection")

def report_sighting():

    click.echo("UFO OR UAP ENCOUNTER REPORT")

    choice = ""
    while (choice != "N") and (choice !="n"):

        if (choice == 'Y') or (choice == 'y'):

            click.echo("Please fill out the following form... \n")

            input_location = click.prompt("Where did the event occur? (City, State)")
            input_time = click.prompt("What time did the event occur? (24-hr clock time)")
            input_date = click.prompt("What was the date? (YYYY-MM-DD)")
            input_duration = click.prompt("For how long did the event continue? (min:sec)")
            input_encounter_type = click.prompt("What type of encounter did you experience? (sighting, greeting, abduction)")
            input_summary = click.prompt("Please enter a brief description of the event")
            input_ufo_shape = click.prompt("What shape was the object?")

            print(f'''
            ENTERED VALUES:
            ----------------------------------------------
                Location:          ->  {input_location}
                Time (HH:MM):      ->  {input_time}
                Date (YYYY-MM-DD:  ->  {input_date}
                Duration (MM:SS):  ->  {input_duration}
                Encounter Type:    ->  {input_encounter_type}
                Summary:           ->  {input_summary}
                Object Shape:      ->  {input_ufo_shape}
            ----------------------------------------------
            ''')

            event = Sighting(location=input_location,
                             time=input_time,
                             date= input_date,
                             duration=input_duration,
                             encounter_type=input_encounter_type,
                             summary=input_summary,
                             ufo_shape=input_ufo_shape)
            
            session.add(event)
            session.commit()

        elif(choice == 'N') or (choice == 'n'):
            print('Returning to main menu...')
            

        choice = click.prompt("Report Encounter? (Y/N): ")


def profile():
    click.echo("....................................")
    choice = ""
    while (choice != 'Q') or (choice != 'q'):
        if (choice == 'Y') or (choice == 'y'):
            click.echo("A new Truther! Initiating a profile...")

            input_username = click.prompt("Select your username", type=str)
            input_base_location = click.prompt("Please enter your base location", type=str)

            print(f'''
                PROFILE SAVED:
                ----------------------------------------------
                    Username:          ->  {input_username}
                    Base Location:     ->  {input_base_location}
                ----------------------------------------------
                ''')
            new_truther = Truther(username = input_username, 
                                base_location = input_base_location)
            session.add(new_truther)
            session.commit()

        elif choice.upper() == "N":
            input_username = click.prompt("Please enter your username to login:", type=str)
            current_truther = input_username
        elif choice.upper() == "Q":
            click.echo('Returning to main menu...')
        
        choice = click.prompt("Welcome! Are you new here? (Y/N)")
           


def search():
    # last_encounter = session.query(Sighting).first()
    # locations = session.query(Sighting.location)
    # by_date = session.query(Sighting).order_by(Sighting.date)
    # query = session.query(Sighting).filter(Sighting.id == "1").all()

    click.echo('What records are you looking for?')
    # click.echo(last_encounter)
    click.prompt('''
            [Date     (1)]  : View by date
            [Location (2)]  : View by location
            [UFO      (3)]  : View by UFO type
            [Encounter(4)]  : View by encounter type
            [Recent   (5)]  : Find most recently reported sighting
            [Common   (6)]  : Find most commonly reported UFO
            [Truthiest(7)]  : Find Truther with most encounters
    ''')
    
   

    
    