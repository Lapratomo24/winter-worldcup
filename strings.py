import colorama
colorama.init()


def show_opening_title():
    '''
    Displays opening title to the terminal
    '''
    print('''
    
█▀▀ ░▀░ █▀▀ █▀▀█ 　 █░░░█ █▀▀█ █▀▀█ █░░ █▀▀▄ 　 █▀▀ █░░█ █▀▀█ 　 █▀█ █▀▀█ █▀█ █▀█ 
█▀▀ ▀█▀ █▀▀ █▄▄█ 　 █▄█▄█ █░░█ █▄▄▀ █░░ █░░█ 　 █░░ █░░█ █░░█ 　 ░▄▀ █▄▀█ ░▄▀ ░▄▀ 
▀░░ ▀▀▀ ▀░░ ▀░░▀ 　 ░▀░▀░ ▀▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀░ 　 ▀▀▀ ░▀▀▀ █▀▀▀ 　 █▄▄ █▄▄█ █▄▄ █▄▄''')


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


def show_closing_remark():
    '''
    Displays closing remark with a soccer ball art
    '''
    print('''
    
▀▀█▀▀ ░▀░ █░░ █░░ 　 █▀▀▄ █▀▀ █░█ ▀▀█▀▀ 　 ▀▀█▀▀ ░▀░ █▀▄▀█ █▀▀ █ 
░▒█░░ ▀█▀ █░░ █░░ 　 █░░█ █▀▀ ▄▀▄ ░░█░░ 　 ░░█░░ ▀█▀ █░▀░█ █▀▀ ▀ 
░▒█░░ ▀▀▀ ▀▀▀ ▀▀▀ 　 ▀░░▀ ▀▀▀ ▀░▀ ░░▀░░ 　 ░░▀░░ ▀▀▀ ▀░░░▀ ▀▀▀ ▄''')


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
    """
    Prints text in red
    """
    colored = f"\033[31m{text}\033[0m"
    print(colored)
