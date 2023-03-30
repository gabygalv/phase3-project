import click
from lib.helpers import report_sighting, search, main_menu_text

def main_menu ():

    choice = ""
    main_menu_text()

    while choice != 'quit' and choice != 'q' and choice != 'Q':
        if (choice in ['r', 'R', 'report']):
            report_sighting()
        if (choice in ['s', 'S', 'search']):
            search()

        choice = click.prompt("Enter selection")

def encounter_counter():
    main_menu()    

    print("Thank you for using Encounter Counter!")

