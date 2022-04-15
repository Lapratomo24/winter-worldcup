import random
import time
import os
import sys
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from colorama import Fore

from strings import opening_title, leaderboard_message, closing_message
from strings import venues_header, group_header, fixture_header, menu_header
from strings import cyan_colored, red_colored, green_colored, quiz_header
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

groups = ["a", "b", "c", "d", "e", "f", "g", "h"]
leaderboard = SHEET.worksheet('leaderboard')
venues = SHEET.worksheet('venues')

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


def clear_terminal():
    '''
    Clears the terminal
    '''
    os.system('clear')


def shut_down():
    '''
    Shuts down the terminal
    '''
    print(2*"\n")
    closing_message()
    sys.exit()


def show_menu():
    '''
    Displays main menu to the user
    '''
    while True:
        menu_header()
        print()
        cyan_colored("Please choose one of the options:\n")
        print("\n(a) World Cup Venues\n")
        print("(b) World Cup National Teams\n")
        print("(c) World Cup Fixtures\n")
        print("(d) World Cup Trivia Quiz\n")
        print("(e) Exit\n")
        user_input = input("")

        if validate_input(user_input):
            print()
            print("Redirecting...")
            time.sleep(1)
            clear_terminal()
            break

    print("Now loading...\n")
    if user_input == ("a"):
        print("Taking you to the list of venues in Qatar...")
        time.sleep(2)
        clear_terminal()
        view_venues()
    if user_input == ("b"):
        print("Taking you to the list of qualified national teams...")
        time.sleep(2)
        clear_terminal()
        view_groups()
    if user_input == ("c"):
        print("Taking you to the upcoming fixtures of FIFA World Cup 2022...")
        time.sleep(2)
        clear_terminal()
        view_fixtures_to_pick()
    if user_input == ("d"):
        print("Ready to put your knowledge to the test?")
        time.sleep(2)
        clear_terminal()
        view_quiz_instruction()
    if user_input == ("e"):
        shut_down()


def return_to_menu():
    '''
    Displays the option to navigate back to main menu
    '''
    while True:
        print("\nPress m then enter to return to main menu.\n")
        print("Press e then enter to exit the terminal.\n")
        user_input = input('')

        if validate_input(user_input):
            print("\nNow loading...")
            time.sleep(1)
            clear_terminal()
            break

    if user_input == "m":
        time.sleep(1)
        clear_terminal()
        show_menu()
    elif user_input == "e":
        shut_down()


def validate_input(input_value):
    """
    Validates user input,
    which otherwise raises Error
    """
    input_value = input_value.lower()
    try:
        if input_value not in {"a", "b", "c", "d", "e", "m", "s"}:
            raise ValueError("Please try again")
    except ValueError as e:
        print(Fore.RED + f'\nInvalid input: {e}.\n')
        print('\033[39m')
        return False

    return True


def view_venues():
    '''
    Displays venue data from worksheet
    '''
    venues_header()
    print()
    venues_list = venues.get_all_values()
    print(tabulate(venues_list, headers="firstrow", tablefmt="rst"))
    print()
    return_to_menu()


def view_groups():
    '''
    Displays all group participating in World Cup 2022
    '''
    while True:
        cyan_colored("Please choose from one of the groups:\n")
        for group in groups:
            print("(" + group + ") Group " + group.upper())
            print()

        group_input = input("").lower()
        if group_input not in groups:
            red_colored("\nInvalid input. Choose from one of the options.\n")
        else:
            break

    clear_terminal()
    print("Now loading...\n")
    time.sleep(1)
    print("Taking you to Group " + group_input.upper() + "...")
    time.sleep(1)
    clear_terminal()
    view_group_info(group_input)


def view_group_info(group_name):
    '''
    Displays group fixtures from worksheet
    '''
    group_header()
    print()
    group_sheet = SHEET.worksheet('group_' + group_name)
    display_group = group_sheet.get_all_values()
    print(tabulate(display_group, headers="firstrow", tablefmt="github"))
    print()
    return_to_menu()


def view_fixtures_to_pick():
    '''
    Displays all group fixtures for World Cup 2022
    '''
    while True:
        cyan_colored("Please choose from one of the groups:\n")
        for group in groups:
            print("(" + group + ") Group " + group.upper())
            print()

        group_input = input("").lower()
        if group_input not in groups:
            red_colored("\nInvalid input. Choose from one of the options.\n")
        else:
            break

    clear_terminal()
    print("Now loading...\n")
    time.sleep(1)
    print("Taking you to Group " + group_input.upper() + " fixtures...")
    time.sleep(1)
    clear_terminal()
    view_fixture(group_input)


def view_fixture(group_name):
    '''
    Displays group fixtures from worksheet
    '''
    fixture_header()
    print()
    fixture_sheet = SHEET.worksheet('fixture_' + group_name)
    display_fixture = fixture_sheet.get_all_values()
    print(tabulate(display_fixture, headers="firstrow", tablefmt="github"))
    print()
    return_to_menu()


def view_quiz_instruction():
    '''
    Displays simple instruction for the quiz to the user
    '''
    print()
    quiz_header()
    print(3*"\n")
    print("Let's test your knowledge for a bit, shall we? ;)\n\n".center(80))
    cyan_colored("There are 10 questions for you to answer.\n".center(80))
    cyan_colored("You get 10 points for each correct answer.\n\n".center(80))
    while True:
        print("Press s to start when you're ready. Good Luck!\n".center(80))
        user_input = input(''.center(37))

        if validate_input(user_input):
            print()
            print("Redirecting...".center(80))
            time.sleep(1)
            clear_terminal()
            break

    if user_input == "s":
        print("\nLoading the quiz...")
        time.sleep(1)
        clear_terminal()
        view_trivia_quiz()


def view_trivia_quiz():
    '''
    Displays the questions and counts total score achieved by the user
    '''
    score = 0
    correct = 0
    incorrect = 0
    selected_questions = random.sample(quiz_list, 10)
    for quiz in selected_questions:
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
    time.sleep(2)
    green_colored(f'{correct} correct answers.')
    red_colored(f'{incorrect} incorrect answers.')
    print()
    print(f'Your total score: {score}')
    print("\nEnter your name to see it on the leaderboard:\n")
    name = input("")
    time.sleep(1)
    leaderboard.append_row(values=[name, correct, incorrect, score])
    clear_terminal()
    view_leaderboard()


def view_leaderboard():
    '''
    Displays a simple leaderboard to show total scores for trivia quiz
    '''
    leaderboard_message()
    print()
    participants = leaderboard.get_all_values()
    print(tabulate(participants, headers="firstrow", tablefmt="simple"))
    print()
    return_to_menu()


def name_input():
    '''
    Takes user name input
    '''
    try:
        print("Type in your name then press enter:\n".center(80))
        name = input("".center(37))
        if not name:
            raise ValueError
        else:
            print()
            cyan_colored(f'Hello {name}, and welcome!'.center(80))
            print()
    except ValueError:
        print(Fore.RED + 'Please enter a valid name.\n'.center(80))
        print('\033[39m')
        name_input()


def main():
    '''
    Runs all functions
    '''
    opening_title()
    print()
    cyan_colored("The first ever Winter World Cup is coming!".center(80))
    cyan_colored("Hope you're as excited to watch it as I am!".center(80))
    print()
    name_input()
    print("Loading main menu...".center(80))
    time.sleep(2)
    clear_terminal()
    show_menu()


main()
