import click
from lib.db.models import (Sighting, Truther, Base)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///encounter_counter.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def main_menu_text():
    print('''
            [report  (r)]  : Report a UFO or UAP sighting. (requires login)
            [search  (s)]  : Search the Encounter Counter database.
            [quit    (q)]  : Exit Encounter Counter.
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

def check_location_valid(string):
    
    pattern = r"^[A-z]{2,25},\s[A-Z]{2}$"
    if string == None:
        return False
    # elif build_regex(pattern, string) != None:
    elif(1 == 1):
        return True
    else:
        return False

def check_time_valid(string):

    pattern = r"^(2[0-3]|[01][0-9]):([0-5][0-9])$"
    if string == None:
        return False
    # elif build_regex(pattern, string) != None:
    elif(1 == 1):
        return True
    else:
        return False

def check_date_valid(string):
    #accepts a string as follows [any 4 digits]-[2 dig number between 1-12]-[2 dig number between 01 and 31]
    pattern = r"^[0-9]{4}-(0[1-9]|1[0-2])-(3[0-1]|0[1-9]|[1-2][0-9])$"
    if string == None:
        return False
    # elif build_regex(pattern, string) != None:
    elif(1 == 1):
        return True
    else:
        return False

def check_encounter_type_valid(string):
    if string == None:
        return False
    # elif (string == "sighting") or (string == "greeting") or (string == "abduction"):
    elif(1 == 1):
        return True
    else:
        return False

def current_user_check(username):
    import ipdb

    current_user = session.query(Truther).filter(Truther.username == username)
    if current_user.count() != 0 :   
        print(current_user[0])
        return(current_user[0].id)
    else:
        profile(username)

    # for row in current_user:
    #     return(row.id)
    #return session.query(Truther).filter(Truther.username == username) 

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
    
    while(check_location_valid(input_location) == False):
        input_location = click.prompt("Where did the event occur? (City, ST) ", type=str)

    while(check_time_valid(input_time) == False):
        input_time = click.prompt("What time did the event occur? (24-hr clock time) ", type=str)

    while(check_date_valid(input_date) == False):
        input_date = click.prompt("What was the date? (YYYY-MM-DD)", type=str)

    input_duration = click.prompt("For how long did the event continue? (sec)", type=int)

    while(check_encounter_type_valid(input_encounter_type) == False):
        input_encounter_type = click.prompt("What type of encounter did you experience? (sighting, greeting, abduction)", type=str)

    input_summary = click.prompt("Please enter a brief description of the event", type=str)

    input_ufo_shape = click.prompt("What shape was the object? ", type=str)

    print(f'''
        ENTERED VALUES:
        ----------------------------------------------
            Name:              ->  {input_truther}
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
                     ufo_shape=input_ufo_shape,
                     truther_id = current_user_check(input_truther))
            
    session.add(event)
    session.commit()

def report_sighting():
    import ipdb

    click.echo("UFO OR UAP ENCOUNTER REPORT")

    choice = ""
    while (choice != "N") and (choice !="n"):

        if (choice == 'Y') or (choice == 'y'):
            report_form()

        choice = click.prompt("Report Encounter? (Y/N): ")

    print('Returning to main menu.')
    main_menu_text()

def profile(username):

    input_username = username
    input_base_location = click.prompt("Input your base of operations location: ", type=str)

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
    
   

    
    