import random
import time
import os
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

from strings import show_opening_title
from strings import cyan_colored, red_colored, green_colored
from quiz import Trivia, trivia_quizzes


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('winter_world_cup')

GROUP_FIXTURES = ["a", "b", "c", "d", "e", "f", "g", "h"]
leaderboard = SHEET.worksheet('leaderboard')
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
        print("\n(a) World Cup Venues\n")
        print("(b) World Cup Groups & Fixtures\n")
        print("(c) World Cup Trivia Quiz\n")
        user_input = input("")

        if validate_input(user_input):
            print()
            print("Redirecting...")
            clear_terminal()
            break

    print("\nNow loading...")
    if user_input == ("a"):
        print("Taking you to the list of venues in Qatar...")
        clear_terminal()
        view_venues()
    if user_input == ("b"):
        print("Taking you to the upcoming fixtures of FIFA World Cup 2022...")
        clear_terminal()
        view_fixtures_to_pick()
    if user_input == ("c"):
        print("Ready to put your knowledge to the test?")
        clear_terminal()
        view_trivia_quiz(quiz_list)


def return_to_menu():
    '''
    Displays the option to navigate back to main menu
    '''
    while True:
        print("\nPress m then enter to return to main menu\n")
        user_input = input('')

        if validate_input(user_input):
            print("Redirecting you back to main menu...")
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
        for group in GROUP_FIXTURES:
            print("(" + group + ") Group " + group.upper())

        group_input = input("").lower()
        if group_input not in GROUP_FIXTURES:
            red_colored("Invalid input. Choose from one of the options.")
        else:
            break

    clear_terminal()
    print("\nNow loading...\n")
    print("Taking you to Group " + group_input.upper() + " fixtures...")
    clear_terminal()
    view_fixture(group_input)

def

def view_fixture(group_name):
    '''
    Displays group fixtures from worksheet
    '''
    fixture_sheet = SHEET.worksheet('fixture_' + group_name)
    display_fixture = fixture_sheet.get_all_values()
    print(tabulate(display_fixture, headers="firstrow", tablefmt="github"))
    print()
    return_to_menu()


quiz_list = [
    Trivia(trivia_quizzes[0], "b"),
    Trivia(trivia_quizzes[1], "c"),
    Trivia(trivia_quizzes[2], "a"),
    Trivia(trivia_quizzes[3], "c"),
    Trivia(trivia_quizzes[4], "c"),
    Trivia(trivia_quizzes[5], "a"),
    Trivia(trivia_quizzes[6], "b"),
    Trivia(trivia_quizzes[7], "b"),
    Trivia(trivia_quizzes[8], "c"),
    Trivia(trivia_quizzes[9], "a"),
    Trivia(trivia_quizzes[10], "b"),
    Trivia(trivia_quizzes[11], "a"),
]


def view_trivia_quiz(quiz_list):
    '''
    Displays the questions and counts total score from user
    '''
    score = 0
    correct = 0
    incorrect = 0
    random.shuffle(quiz_list)
    for quiz in quiz_list:
        while True:
            user_answers = input(quiz.question).lower()
            if user_answers not in {"a", "b", "c"}:
                red_colored("\nPlease enter a valid input.\n")
            else:
                break
        if user_answers == quiz.answer:
            green_colored("\nCorrect!\n")
            score += 10
            correct += 1
        else:
            red_colored("\nIncorrect.\n")
            incorrect += 1
    green_colored(f'{correct} correct answers.')
    red_colored(f'{incorrect} incorrect answers.')
    print()
    print(f'Your total score: {score}')
    print()
    return_to_menu()


def name_input():
    '''
    Takes user name input
    '''
    try:
        name = input("Type in your name then press Enter:\n\n")
        if not name:
            raise ValueError
        else:
            cyan_colored(f'Hello {name}, and welcome!\n')
    except ValueError:
        print('Please enter a valid name')
        name_input()


def main():
    '''
    Runs all functions
    '''
    show_opening_title()
    cyan_colored("\nThe first ever Winter World Cup Is Coming..\n")
    name_input()
    clear_terminal()
    show_menu()


main()

