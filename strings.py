import colorama
colorama.init()


def show_opening_title():
    '''
    Displays opening title to the terminal
    '''
    print('''
█░█░█ █▀█ █▀█ █░░ █▀▄   █▀▀ █░█ █▀█   ▀█ █▀█ ▀█ ▀█
▀▄▀▄▀ █▄█ █▀▄ █▄▄ █▄▀   █▄▄ █▄█ █▀▀   █▄ █▄█ █▄ █▄\n''')


def show_closing_remark():
    '''
    Displays closing remark with a soccer ball art
    '''
    print('''
                         ___
 o__        o__     |   |\\
/|          /\      |   |X\\
/ > o        <\     |   |XX\\\n''')


def cyan_colored(text):
    '''
    Prints text in cyan
    '''
    colored = f"\033[36;1m{text}\033[0m"
    print(colored)

def red_colored(text):
    """
    Prints text in red
    """
    colored = f"\033[31m{text}\033[0m"
    print(colored)