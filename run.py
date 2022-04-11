import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
import random
import os
import time

from strings import show_opening_title, show_closing_remark, cyan_colored, red_colored

GROUP_NAMES = ["a", "b", "c", "d", "e", "f", "g", "h"]

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


def clear_terminal():
    '''
    Clears the terminal
    '''
    os.system('clear')


def show_menu():
    '''
    Displays main menu to the user
    '''
    while True:
        cyan_colored("Please choose one of the options:\n")
        print("\n(a) World Cup Venues")
        print("(b) World Cup Groups & Fixtures\n")
        user_input = input("")

        if validate_input(user_input):
            print()
            print("Redirecting..!")
            clear_terminal()
            break

    print("\nNow loading...")
    if user_input == ("a"):
        print("Taking you to list of venues in Qatar...")
        clear_terminal()
        view_venues()
    if user_input == ("b"):
        print("Taking you to upcoming fixtures for FIFA World Cup 2022...")
        clear_terminal()
        view_fixtures_to_pick()


def return_to_menu():
    '''
    Displays the option to navigate back to main menu
    '''
    while True:
        print("\nPress m then enter to return to main menu\n")
        user_input = input('')

        if validate_input(user_input):
            print("Redirecting you back to main menu..!")
            clear_terminal()
            break

    if user_input == "m":
        print("\nNow loading...")
        clear_terminal()
        show_menu()


def validate_input(input_value):
    """
    Validates user input,
    which otherwise raises Error
    """
    input_value = input_value.lower()
    try:
        [value for value in input_value]
        if input_value not in {"a", "b", "c", "m"}:
            raise ValueError("Please try again.")
    except ValueError as e:
        print(f'Invalid input: {e}.\n')
        return False

    return True


def view_venues():
    '''
    Displays venue data from worksheet
    '''
    venues_list = venues.get_all_values()
    print(tabulate(venues_list, headers="firstrow", tablefmt="rst"))
    print()
    return_to_menu()


def view_fixtures_to_pick():
    '''
    Displays all group fixtures for World Cup 2022
    '''
    while True:
        cyan_colored("\nPlease choose from one of the groups:\n")
        for group in GROUP_NAMES:
            print("(" + group + ") Group " + group.upper())

        group_input = input("").lower()
        if group_input not in GROUP_NAMES:
            red_colored("Invalid input. Choose from one of the options.")
        else:
            break

    clear_terminal()
    print("\nNow loading...\n")
    print("Taking you to Group " + group_input.upper() + " fixtures...")
    clear_terminal()
    view_fixture(group_input)


def view_fixture(group_name):
    '''
    Displays group a fixtures from worksheet
    '''
    fixture_sheet = SHEET.worksheet('fixture_' + group_name)
    display_fixture = fixture_sheet.get_all_values()
    print(tabulate(display_fixture, headers="firstrow", tablefmt="github"))
    print()
    return_to_menu()


def take_user_name():
    try:
        name = input("Type in your name then press Enter:\n\n")
        if not name:
            raise ValueError
        else:
            cyan_colored(f'Hello {name}, and welcome!\n')
    except ValueError:
        print('Please enter a valid name')
        take_user_name()


def main():
    show_opening_title()
    cyan_colored("The first ever Winter World Cup Is Coming..\n")
    take_user_name()
    clear_terminal()
    show_menu()


main()
