import colorama
colorama.init()

def opening_title():
    '''
    Displays opening title to the terminal
    '''
    print('''
    
█░█░█ █▀█ █▀█ █░░ █▀▄   █▀▀ █░█ █▀█   ▀█ █▀█ ▀█ ▀█
▀▄▀▄▀ █▄█ █▀▄ █▄▄ █▄▀   █▄▄ █▄█ █▀▀   █▄ █▄█ █▄ █▄\n''')


def closing_remark():
    '''
    Displays closing remark with a soccer ball art
    '''
    print('''
                         ___
 o__        o__     |   |\
/|          /\      |   |X\
/ > o        <\     |   |XX\\n''')


def cyan_colored(text):
    '''
    Prints text in cyan
    '''
    colored = f"\033[36;1m{text}\033[0m"
    print(colored)