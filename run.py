import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
import random
import os
import time

from strings import opening_title, closing_remark
from strings import cyan_colored

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('winter_world_cup')

venues = SHEET.worksheet('venues')
groups = SHEET.worksheet('groups')
fixture_a = SHEET.worksheet('fixture_a')
fixture_b = SHEET.worksheet('fixture_b')
fixture_c = SHEET.worksheet('fixture_c')
fixture_d = SHEET.worksheet('fixture_d')
fixture_e = SHEET.worksheet('fixture_e')
fixture_f = SHEET.worksheet('fixture_f')
fixture_g = SHEET.worksheet('fixture_g')
fixture_h = SHEET.worksheet('fixture_h')

def clear_terminal():
    '''
    Clears the terminal
    '''
    os.system('clear')

def menu():
    '''
    Displays main menu to the user
    '''
    while True:
        cyan_colored(f'Hello {name}, and welcome!\n')
        cyan_colored("Please choose one of the options below:\n")
        print()
        print("(a) World Cup Venues")
        print("(b) World Cup Groups")
        print("(c) World Cup Fixtures")
        print()
        user_input = input("")

        if validate_input(user_input):
            print("Right on!")
            time.sleep(2)
            clear_terminal()
            break
    
    return user_input

def validate_input(values):
    """
    Validates user input, 
    which otherwise raises Error
    """
    try:
        [value for value in values]
        if values not in {"a", "b", "c", "d"}:
            raise ValueError("Choose one of the above options")
    except ValueError as e:
        print(f'Invalid data: {e}.\n')
        return False
    
    return True

def view_venues():
    '''
    Displays venue data from worksheet
    '''
    display_venues = venues.get_all_values()
    print(tabulate(venues, headers, tablefmt="rst"))
    print()

def view_groups():
    '''
    Displays groups data from worksheet
    '''
    display_groups = groups.get_all_values()
    print(tabulate(groups, headers, tablefmt="rst"))
    print()

def view_fixture_a():
    '''
    Displays group a fixtures from worksheet
    '''
    display_fixture_a = fixture_a.get_all_values()
    print(tabulate(fixture_a, headers, tablefmt="rst"))
    print()

def view_fixture_b():
    '''
    Displays group a fixtures from worksheet
    '''
    display_fixture_b = fixture_b.get_all_values()
    print(tabulate(fixture_b, headers, tablefmt="rst"))
    print()

def view_fixture_c():
    '''
    Displays group a fixtures from worksheet
    '''
    display_fixture_c = fixture_c.get_all_values()
    print(tabulate(fixture_c, headers, tablefmt="rst"))
    print()

def view_fixture_d():
    '''
    Displays group a fixtures from worksheet
    '''
    display_fixture_d = fixture_d.get_all_values()
    print(tabulate(fixture_d, headers, tablefmt="rst"))
    print()

def view_fixture_e():
    '''
    Displays group a fixtures from worksheet
    '''
    display_fixture_e = fixture_e.get_all_values()
    print(tabulate(fixture_e, headers, tablefmt="rst"))
    print()

def view_fixture_f():
    '''
    Displays group a fixtures from worksheet
    '''
    display_fixture_f = fixture_f.get_all_values()
    print(tabulate(fixture_f, headers, tablefmt="rst"))
    print()

def view_fixture_g():
    '''
    Displays group a fixtures from worksheet
    '''
    display_fixture_g = fixture_g.get_all_values()
    print(tabulate(fixture_g, headers, tablefmt="rst"))
    print()

def view_fixture_h():
    '''
    Displays group a fixtures from worksheet
    '''
    display_fixture_h = fixture_h.get_all_values()
    print(tabulate(fixture_h, headers, tablefmt="rst"))
    print()

#if user_input == "a":
        #print("Now loading...")
        #time.sleep(2)
        #print("Taking you to the tournament venues in Qatar...")
        #time.sleep(1)
        #clear_terminal()


opening_title()
cyan_colored("The first ever Winter World Cup Is Coming..\n")
name = input("Type in your name then press Enter:\n")
time.sleep(2)
clear_terminal()
menu()
closing_remark()

