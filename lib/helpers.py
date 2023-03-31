import click
import re
from lib.db.models import (Sighting, Truther, UFO, Base)
from sqlalchemy import create_engine, func
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

def view_report_menu(name, loc, time, date, dur, enc, summ, obj):

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

            view_report(name, loc, time, date, dur, enc, summ, obj)      

        choice = 'd'

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
    elif build_regex(pattern, string) != None:
        return True
    else:
        return False

def verify_time(string):

    pattern = r"^(2[0-3]|[01][0-9]):([0-5][0-9])$"
    if string == None:
        return False
    elif build_regex(pattern, string) != None:
        return True
    else:
        return False

def verify_date(string):
    #accepts a string as follows [any 4 digits]-[2 dig number between 1-12]-[2 dig number between 01 and 31]
    pattern = r"^[0-9]{4}-(0[1-9]|1[0-2])-(3[0-1]|0[1-9]|[1-2][0-9])$"
    if string == None:
        return False
    elif build_regex(pattern, string) != None:
        return True
    else:
        return False

def verify_encounter_type(string):
    if string == None:
        return False
    elif (string == "sighting") or (string == "greeting") or (string == "abduction"):
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


def check_if_new_user(username):

    current_user = session.query(Truther).filter(Truther.username == username)
    if current_user.count() != 0 :
        return(current_user[0].id)
    else:
        profile(username)
        current_user = session.query(Truther).filter(Truther.username == username)
        return(current_user[0].id)

def check_if_new_ufo(new_shape):
    ufo_shape = session.query(UFO).filter(UFO.shape == new_shape)
    if ufo_shape.count() != 0:
        return(ufo_shape[0].id)
    else:
        new_ufo = UFO(shape=new_shape)
        session.add(new_ufo)
        session.commit()

        ufo_shape = session.query(UFO).filter(UFO.shape == new_shape)
        return(ufo_shape[0].id)        

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
    
    input_ufo_id = check_if_new_ufo(input_ufo_shape)
    input_truther_id = check_if_new_user(input_truther)

    event = Sighting(location=input_location,
                     time=input_time,
                     date= input_date,
                     duration=input_duration,
                     encounter_type=input_encounter_type,
                     summary=input_summary,
                     ufo_id=input_ufo_id,
                     truther_id = input_truther_id)
            
    session.add(event)
    session.commit()

    view_report_menu(input_truther, input_location,
                     input_time, input_date, input_duration,
                     input_encounter_type, input_summary,
                     input_ufo_shape)

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

def search_date():

    by_date=session.query(Sighting).order_by(Sighting.date).limit(10).all()
    click.echo([date for date in by_date])

def search_year():
    input_year = click.prompt("Enter the year you want to find encounters in")
    by_year=session.query(Sighting)\
        .filter(Sighting.date\
        .contains(input_year))

    if by_year.count() != 0:
        click.echo([year for year in by_year])
    else:
        click.echo(f"No encounters reported in {input_year}")

def search_loc():
    input_location = click.prompt("Enter the location you want to find encounters in")
    by_location=session.query(Sighting)\
        .filter(Sighting.location\
        .contains(input_location))

    if by_location.count() != 0:
        click.echo([location for location in by_location])
    else:
        click.echo(f"No encounters reported in {input_location}")

def search_ufo():
    input_shape = click.prompt("Enter a UFO shape to search by (-o to view suggestions)")
    by_shape = session.query(Sighting, UFO)\
        .join(UFO).where(UFO.shape == input_shape\
        .capitalize())

    if by_shape.count() != 0:
        click.echo([shape[0] for shape in by_shape])
    else:
        click.echo(f"No encounters reported for {input_shape}")

def search_encounter():
    input_encounter = click.prompt("Enter one of the following encounter types to search for: sighting, greeting, abduction)")
    by_type = session.query(Sighting)\
        .filter(Sighting.encounter_type\
        .contains(input_encounter.capitalize()))

    click.echo([type for type in by_type])

def search_most_rec():
    recent = session.query(Sighting)\
        .order_by((Sighting.id).desc()).limit(1)

    click.echo([recent for recent in recent])

def search_most_common():
    most_common = session.query(UFO, func.count(Sighting.ufo_id))\
        .join(Sighting).group_by(UFO.id)\
        .order_by(func.count(Sighting.ufo_id)\
        .desc()).limit(1)

    print(f"{most_common[0][0].shape} shaped UFO was reported {most_common[0][1]} times")

def search_truthiest():
    truthiest = session.query(Truther, func.count(Sighting.truther_id))\
        .join(Sighting).group_by(Truther.id)\
        .order_by(func.count(Sighting.truther_id)\
        .desc()).limit(1)

    print(f'''
        The truthiest truther is {truthiest[0][0].username}.
        They've reported {truthiest[0][1]} encounters.
        {truthiest[0][0].username} is based in {truthiest[0][0].base_location}.
    ''')

def search_menu_text ():
    click.echo('''
            [Date     (1)]  : View 10 oldest encounters
            [Year     (2)]  : View encounters by specified year
            [Location (3)]  : View by location
            [UFO      (4)]  : View by UFO type
            [Encounter(5)]  : View by encounter type
            [Recent   (6)]  : Find most recently reported sighting
            [Common   (7)]  : Find most commonly reported UFO
            [Truthiest(8)]  : Find Truther with most encounters
            [Quit     (q)]  : Return to the main menu.
        ''')

def search():

    choice = ''
    while choice not in ['q', 'Q', 'quit', 'Quit']:

        if choice == "1":
            search_date()
        elif choice == "2":
            search_year()
        elif choice == "3":
            search_loc()
        elif choice == "4":
            search_ufo()
        elif choice == "5":
            search_encounter()
        elif choice == "6":
            search_most_rec()
        elif choice == "7":
            search_most_common()
        elif choice == "8":
            search_truthiest()

        search_menu_text ()
        choice = click.prompt("What records are you looking for?")
    
    main_menu_text()
