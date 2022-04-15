import colorama
colorama.init()


def opening_title():
    '''
    Displays opening title to the terminal
    '''
    title = '''
    
─╔═╗─╔═╗─────────────╔╗──╔╗──────────╔═══╦═══╦═══╦═══╗
─║╔╝─║╔╝─────────────║║──║║──────────║╔═╗║╔═╗║╔═╗║╔═╗║
╔╝╚╦╦╝╚╦══╗╔╗╔╗╔╦══╦═╣║╔═╝║╔══╦╗╔╦══╗╚╝╔╝║║║║╠╝╔╝╠╝╔╝║
╚╗╔╬╬╗╔╣╔╗║║╚╝╚╝║╔╗║╔╣║║╔╗║║╔═╣║║║╔╗║╔═╝╔╣║║║╠═╝╔╬═╝╔╝
─║║║║║║║╔╗║╚╗╔╗╔╣╚╝║║║╚╣╚╝║║╚═╣╚╝║╚╝║║║╚═╣╚═╝║║╚═╣║╚═╗
─╚╝╚╝╚╝╚╝╚╝─╚╝╚╝╚══╩╝╚═╩══╝╚══╩══╣╔═╝╚═══╩═══╩═══╩═══╝
─────────────────────────────────║║
─────────────────────────────────╚╝'''
    print('\n'.join(title.center(80) for title in title.splitlines()))


def quiz_header():
    '''
    Displays header for trivia quiz
    '''
    header = '''

█░█░█ █▀█ █▀█ █░░ █▀▄   █▀▀ █░█ █▀█   ▀█▀ █▀█ █ █░█ █ ▄▀█   █▀█ █░█ █ ▀█
▀▄▀▄▀ █▄█ █▀▄ █▄▄ █▄▀   █▄▄ █▄█ █▀▀   ░█░ █▀▄ █ ▀▄▀ █ █▀█   ▀▀█ █▄█ █ █▄'''
    print('\n'.join(header.center(80) for header in header.splitlines()))


def leaderboard_message():
    '''
    Display message above leaderboard
    '''
    print('''
    
╔╗╔╗──────╔╗╔═╗╔═╗───────────╔╗╔╗─╔╗────╔╗╔╗────╔╗
║╚╣╚╦═╗╔═╦╣╠╣═╣║═╬═╦╦╗╔═╦═╗╔╦╣╚╬╬═╬╬═╦═╗║╚╬╬═╦╦═╣║
║╔╣║║╬╚╣║║║═╬═║║╔╣╬║╔╝║╬║╬╚╣╔╣╔╣║═╣║╬║╬╚╣╔╣║║║║╬║║
╚═╩╩╩══╩╩═╩╩╩═╝╚╝╚═╩╝─║╔╩══╩╝╚═╩╩═╩╣╔╩══╩═╩╩╩═╬╗╠╣
──────────────────────╚╝───────────╚╝─────────╚═╩╝''')


def closing_message():
    '''
    Displays closing remark with a soccer ball art
    '''
    title = '''
    
▀█▀ █ █░░ █░░   █▄░█ █▀▀ ▀▄▀ ▀█▀   ▀█▀ █ █▀▄▀█ █▀▀ █
░█░ █ █▄▄ █▄▄   █░▀█ ██▄ █░█ ░█░   ░█░ █ █░▀░█ ██▄ ▄'''
    print('\n'.join(title.center(80) for title in title.splitlines()))
    print()
    football = '''
                        ___
o__        o__     |   |\\
/|          /\      |   |X\\
/ > o        <\     |   |XX\\'''
    print('\n'.join(football.center(80) for football in football.splitlines()))
        

def venues_header():
    '''
    Displays header for venues
    '''
    print('''
█░█ █▀▀ █▄░█ █░█ █▀▀ █▀
▀▄▀ ██▄ █░▀█ █▄█ ██▄ ▄█''')


def group_header():
    '''
    Displays header for groups
    '''
    print('''
▀█▀ █▀▀ ▄▀█ █▀▄▀█ █▀
░█░ ██▄ █▀█ █░▀░█ ▄█''')


def fixture_header():
    '''
    Displays header for fixtures
    '''
    print('''
█▀▀ █ ▀▄▀ ▀█▀ █░█ █▀█ █▀▀ █▀
█▀░ █ █░█ ░█░ █▄█ █▀▄ ██▄ ▄█''')


def menu_header():
    '''
    Displays header for main menu
    '''
    print('''
█▀▄▀█ ▄▀█ █ █▄░█   █▀▄▀█ █▀▀ █▄░█ █░█
█░▀░█ █▀█ █ █░▀█   █░▀░█ ██▄ █░▀█ █▄█
    ''')


def cyan_colored(text):
    '''
    Prints text in cyan
    '''
    colored = f"\033[36;1m{text}\033[0m"
    print(colored)


def green_colored(text):
    '''
    Prints text in cyan
    '''
    colored = f"\033[32;1m{text}\033[0m"
    print(colored)


def red_colored(text):
    '''
    Prints text in red
    '''
    colored = f"\033[31m{text}\033[0m"
    print(colored)
