import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
import random
import os
import time

from strings import opening_title, closing_remark
from strings import cyan_colored, red_colored

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
        cyan_colored("Please choose one of the options:\n")
        print()
        print("(𝕒) Wᴏʀʟᴅ Cᴜᴘ Vᴇɴᴜᴇs")
        print("(b) Wᴏʀʟᴅ Cᴜᴘ Gʀᴏᴜᴘs & Fɪxᴛᴜʀᴇs")
        print()
        user_input = input("")

        if validate_input(user_input):
            print("Right on!")
            time.sleep(1)
            clear_terminal()
            break
    
    if user_input == ("a"):
        print()
        print("Now loading...")
        time.sleep(1)
        print()
        print("Taking you to list of venues in Qatar...")
        time.sleep(2)
        clear_terminal()
        view_venues()
    if user_input == ("b"):
        print()
        print("Now loading...")
        time.sleep(1)
        print()
        print("Taking you to upcoming fixtures for FIFA World Cup 2022...")
        time.sleep(2)
        clear_terminal()
        view_fixtures_to_pick()


def validate_input(values):
    """
    Validates user input, 
    which otherwise raises Error
    """
    try:
        [value for value in values]
        if values not in {"a", "b", "c"}:
            raise ValueError("Choose one of the options")
    except ValueError as e:
        print(f'Invalid data: {e}.\n')
        return False
    
    return True


def view_venues():
    '''
    Displays venue data from worksheet
    '''
    venues_list = venues.get_all_values()
    print(tabulate(venues_list, headers="firstrow", tablefmt="rst"))
    print()


def view_fixtures_to_pick():
    '''
    Displays all group fixtures for World Cup 2022
    '''
    while True:
        print()
        cyan_colored("Please choose from one of the groups:\n")
        print()
        print("(𝕒) Gʀᴏᴜᴘ A")
        print("(𝕓) Gʀᴏᴜᴘ B")
        print("(𝕔) Gʀᴏᴜᴘ C")
        print("(𝕕) Gʀᴏᴜᴘ D")
        print("(𝕖) Gʀᴏᴜᴘ E")
        print("(𝕗) Gʀᴏᴜᴘ F")
        print("(𝕘) Gʀᴏᴜᴘ G")
        print("(𝕙) Gʀᴏᴜᴘ H")
        print()
        user_input = input("")
        print()
        if user_input not in {"a", "b", "c", "d", "e", "f", "g", "h"}:
            red_colored("Invalid input. Choose from one of the options.")
        else:
            break
    
    if user_input == ("a"):
        clear_terminal()
        print()
        print("Now loading...")
        time.sleep(1)
        print()
        print("Taking you to Group A fixtures...")
        time.sleep(2)
        clear_terminal()
        view_fixture_a()
    if user_input == ("b"):
        clear_terminal()
        print()
        print("Now loading...")
        time.sleep(1)
        print()
        print("Taking you to Group B fixtures...")
        time.sleep(2)
        clear_terminal()
        view_fixture_b()
    if user_input == ("c"):
        clear_terminal()
        print()
        print("Now loading...")
        time.sleep(1)
        print()
        print("Taking you to Group C fixtures...")
        time.sleep(2)
        clear_terminal()
        view_fixture_c()
    if user_input == ("d"):
        clear_terminal()
        print()
        print("Now loading...")
        time.sleep(1)
        print()
        print("Taking you to Group D fixtures...")
        time.sleep(2)
        clear_terminal()
        view_fixture_d()
    if user_input == ("e"):
        clear_terminal()
        print()
        print("Now loading...")
        time.sleep(1)
        print()
        print("Taking you to Group E fixtures...")
        time.sleep(2)
        clear_terminal()
        view_fixture_e()
    if user_input == ("f"):
        clear_terminal()
        print()
        print("Now loading...")
        time.sleep(1)
        print()
        print("Taking you to Group F fixtures...")
        time.sleep(2)
        clear_terminal()
        view_fixture_f()
    if user_input == ("g"):
        clear_terminal()
        print()
        print("Now loading...")
        time.sleep(1)
        print()
        print("Taking you to Group G fixtures...")
        time.sleep(2)
        clear_terminal()
        view_fixture_g()
    if user_input == ("h"):
        clear_terminal()
        print()
        print("Now loading...")
        time.sleep(1)
        print()
        print("Taking you to Group H fixtures...")
        time.sleep(2)
        clear_terminal()
        view_fixture_h()


def view_fixture_a():
    '''
    Displays group a fixtures from worksheet
    '''
    display_fixture_a = fixture_a.get_all_values()
    print(tabulate(display_fixture_a, headers="firstrow", tablefmt="fancy_grid"))
    print()


def view_fixture_b():
    '''
    Displays group b fixtures from worksheet
    '''
    display_fixture_b = fixture_b.get_all_values()
    print(tabulate(display_fixture_b, headers="firstrow", tablefmt="fancy_grid"))
    print()


def view_fixture_c():
    '''
    Displays group c fixtures from worksheet
    '''
    display_fixture_c = fixture_c.get_all_values()
    print(tabulate(display_fixture_c, headers="firstrow", tablefmt="fancy_grid"))
    print()


def view_fixture_d():
    '''
    Displays group d fixtures from worksheet
    '''
    display_fixture_d = fixture_d.get_all_values()
    print(tabulate(display_fixture_d, headers="firstrow", tablefmt="fancy_grid"))
    print()


def view_fixture_e():
    '''
    Displays group e fixtures from worksheet
    '''
    display_fixture_e = fixture_e.get_all_values()
    print(tabulate(display_fixture_e, headers="firstrow", tablefmt="fancy_grid"))
    print()


def view_fixture_f():
    '''
    Displays group f fixtures from worksheet
    '''
    display_fixture_f = fixture_f.get_all_values()
    print(tabulate(display_fixture_f, headers="firstrow", tablefmt="fancy_grid"))
    print()


def view_fixture_g():
    '''
    Displays group g fixtures from worksheet
    '''
    display_fixture_g = fixture_g.get_all_values()
    print(tabulate(display_fixture_g, headers="firstrow", tablefmt="fancy_grid"))
    print()


def view_fixture_h():
    '''
    Displays group h fixtures from worksheet
    '''
    display_fixture_h = fixture_h.get_all_values()
    print(tabulate(display_fixture_h, headers="firstrow", tablefmt="fancy_grid"))
    print()


opening_title()
cyan_colored("The first ever Winter World Cup Is Coming..\n")
name = input("Type in your name then press Enter:\n\n")
time.sleep(2)
clear_terminal()
menu()

