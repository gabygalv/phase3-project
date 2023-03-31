import click
import time
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
    click.echo("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    click.echo("Thank you for using Encounter Counter!")
    click.echo("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    time.sleep(1.5)
    click.echo("ALERT!!!")
    time.sleep(.5)
    click.echo("Our servers are unstable, your base location may been compromi--")
    time.sleep(1)
    click.echo("""
                _____
             ,-"     "-.
            / o       o \u005c
           /   \     /   \u005c
          /     )-"-(     \u005c
         /     ( 6 6 )     \u005c
        /       \ " /       \u005c
       /         )=(         \u005c
      /   o   .--"-"--.   o   \u005c
     /    I  /  -   -  \  I    \u005c
 .--(    (_}y/\       /\y{_)    )--.
(    ".___l\/__\_____/__\/l___,"    )
 \                                 /
  "-._      o O o O o O o      _,-"
      `--Y--.___________.--Y--'
         |==.___________.==| 
         `==.___________.==' 
    """)
    time.sleep(.5)
    click.echo("Greetings, human! I am Zorax, your Uber driver for today")
    time.sleep(.5)
    click.echo("...")
    time.sleep(1)
    click.echo("What do you mean you didn't order an intergalacic Uber?!?")
    time.sleep(.5)
    click.echo("...")
    time.sleep(.75)
    click.echo("ahh, my navigation system is acting up again...")
    time.sleep(1)
    click.echo("...")
    time.sleep(.5)
    click.echo("Well.. nice to meet you. GTG!")
    time.sleep(1)
    click.echo("""
     .              +   .                .   . .     .  .
                   .                    .       .     *
  .       *             . .           . . . .  .   .  + .
            .     .       .   .    .   .  +  . . .
.                 .              .  .   .    .    . .
    .     .     . +.    +  .        .     .     . +.    +  .
     .       .   . .     . .       .       .   . .
        . .                 .    * . . .  .  +   .
           +      .           .   .      +
                            .       . +  .+. .
  .                      .     . + .  . .     .      .
           .      .    .     . .   . . .        ! /
      *             .    . .  +    .  .       - O -
          .     .    .  +   . .  *  .       . / |
               . + .  .  .  .. +  .
.      .  .  .  *   .  *  . +..  .            *
 .      .   . .   .   .   . .  +   .    .            +
    """)
    time.sleep(.5)
    click.echo("Type 'encounter' to restart Encounter Counter")
