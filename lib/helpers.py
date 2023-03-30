import click
import re
from lib.db.models import (Sighting, Truther, UFO, Base)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///encounter_counter.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def main_menu_text():
    click.echo('''
        .__________________.
        |  Main Menu       |
        |__________________|
        |  report     (r)  |
        |  search     (s)  |
        |  quit       (q)  |       
        |__________________|
         ''')

def build_regex(pattern, string):

    regex = re.compile(pattern)
    match = regex.search(string)

    return match

def main_menu ():

    choice = ""
    main_menu_text()

    while choice != 'quit' and choice != 'q':
        if (choice == 'r') or (choice == 'report'):
            report_sighting()
        if (choice == 's') or (choice == 'search'):
            search()

        choice = click.prompt("Enter selection")

def view_report(name, loc, time, date, dur, enc, summ, obj):
    
    print(f'''
        ._____________________________________________ __ __ _ _ _ _    
        |    ENCOUNTER REPORT
        |_____________________________________________ __ __ _ _ _ _
        |    Name:              ->  {name}
        |    Location:          ->  {loc}
        |    Time (HH:MM):      ->  {time}
        |    Date (YYYY-MM-DD:  ->  {date}
        |    Duration (MM:SS):  ->  {dur}
        |    Encounter Type:    ->  {enc}
        |    Summary:           ->  {summ}
        |    Object Shape:      ->  {obj}
        |___________________________________________ ___ ___ _ _ _ _
    ''')

def verify_location(string):
    
    pattern = r"^[A-z]{2,25},\s[A-Z]{2}$"
    if string == None:
        return False
    # elif build_regex(pattern, string) != None:
    elif(1 == 1):
        return True
    else:
        return False

def verify_time(string):

    pattern = r"^(2[0-3]|[01][0-9]):([0-5][0-9])$"
    if string == None:
        return False
    # elif build_regex(pattern, string) != None:
    elif(1 == 1):
        return True
    else:
        return False

def verify_date(string):
    #accepts a string as follows [any 4 digits]-[2 dig number between 1-12]-[2 dig number between 01 and 31]
    pattern = r"^[0-9]{4}-(0[1-9]|1[0-2])-(3[0-1]|0[1-9]|[1-2][0-9])$"
    if string == None:
        return False
    # elif build_regex(pattern, string) != None:
    elif(1 == 1):
        return True
    else:
        return False

def verify_encounter_type(string):
    if string == None:
        return False
    # elif (string == "sighting") or (string == "greeting") or (string == "abduction"):
    elif(1 == 1):
        return True
    else:
        return False

def verify_ufo_shape(string):

    if string == '-o':

        print('''
        .______________________________________________.
        |  SUGESTIONS                                  |
        | _____________________________________________|       
        |  circle      disc        fireball   pill     |
        |  light       triangle    sphere     cube     |
        |  pyramid     flash       cylinder   unknown  |
        |______________________________________________|  

        ''')
        return False
    elif string == None:
        return False

    return True


def current_user_check(username):

    current_user = session.query(Truther).filter(Truther.username == username)
    if current_user.count() != 0 :
        return(current_user[0].id)
    else:
        profile(username)
        current_user = session.query(Truther).filter(Truther.username == username)
        return(current_user[0].id)

def check_ufo(new_shape):
    ufo_shape = session.query(UFO).filter(UFO.shape == new_shape)
    if ufo_shape.count() != 0:
        return(ufo_shape[0].shape)
    else:
        new_ufo = UFO(shape=new_shape)
        session.add(new_ufo)
        session.commit()

def report_form():

    click.echo("Please fill out the following form... \n")

    input_truther = None
    input_location = None
    input_time = None
    input_date = None
    input_duration = None
    input_encounter_type = None
    input_summary = None
    input_ufo_shape = None

    input_truther = click.prompt("Please enter your name", type = str)
    
    while(verify_location(input_location) == False):
        input_location = click.prompt("Where did the event occur? (City, ST) ", type=str)

    while(verify_time(input_time) == False):
        input_time = click.prompt("What time did the event occur? (24-hr clock time) ", type=str)

    while(verify_date(input_date) == False):
        input_date = click.prompt("What was the date? (YYYY-MM-DD)", type=str)

    input_duration = click.prompt("For how long did the event continue? (sec)", type=int)

    while(verify_encounter_type(input_encounter_type) == False):
        input_encounter_type = click.prompt("What type of encounter did you experience? (sighting, greeting, abduction)", type=str)

    input_summary = click.prompt("Please enter a brief description of the event", type=str)

    while(verify_ufo_shape(input_ufo_shape) == False):
        input_ufo_shape = click.prompt("What shape was the object? (-o to view suggestions)", type=str)

    choice = None

    while(choice not in ['d', 'D', 'done']):

        click.echo('''
        .__________________.
        |  Report Created  |
        |__________________|
        |  view       (v)  |
        |  done       (d)  |       
        |__________________|
        ''')

        choice = click.prompt("View report?")

        if choice in ['v','V', 'view']:

            view_report(input_truther, input_location,
                        input_time, input_date, input_duration,
                        input_encounter_type, input_summary,
                        input_ufo_shape)

        choice = 'd'

    check_ufo(input_ufo_shape)

    event = Sighting(location=input_location,
                     time=input_time,
                     date= input_date,
                     duration=input_duration,
                     encounter_type=input_encounter_type,
                     summary=input_summary,
                     ufo_shape=input_ufo_shape,
                     truther_id = current_user_check(input_truther))
            
    session.add(event)
    session.commit()

def report_sighting():

    click.echo("UFO OR UAP ENCOUNTER REPORT")

    choice = ""
    while (choice != "N") and (choice !="n"):

        if (choice == 'Y') or (choice == 'y'):
            report_form()

        choice = click.prompt("Report New Encounter? (Y/N) ")

    print('Returning to main menu.')
    main_menu_text()

def profile(username):

    input_username = username
    input_base_location = click.prompt("Looks like you're new here, input your base of operations location to create a profile: ", type=str)

    new_truther = Truther(username = input_username, 
        base_location = input_base_location)

    session.add(new_truther)
    session.commit()

def search():
    # last_encounter = session.query(Sighting).first()
    # locations = session.query(Sighting.location)
    # by_date = session.query(Sighting).order_by(Sighting.date)
    # query = session.query(Sighting).filter(Sighting.id == "1").all()

    click.echo('What records are you looking for?')
    click.prompt('''
            [Date     (1)]  : View by date
            [Location (2)]  : View by location
            [UFO      (3)]  : View by UFO type
            [Encounter(4)]  : View by encounter type
            [Recent   (5)]  : Find most recently reported sighting
            [Common   (6)]  : Find most commonly reported UFO
            [Truthiest(7)]  : Find Truther with most encounters
    ''')
    
   

    
    