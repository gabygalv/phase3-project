import click

from lib.db.models import Truther, UFO, Sighting
from lib.helpers import main_menu, report_sighting

def encounter_counter():
    main_menu()    

    print("Thank you for using Encounter Counter!")

