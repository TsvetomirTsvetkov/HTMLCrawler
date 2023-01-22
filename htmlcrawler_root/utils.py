# External imports
import os

from enum import Enum

# Internal imports


# Constants

HTML_CRAWLER = r'''
 _____ _____ _____ __       _____ _____ _____ _ _ _ __    _____ _____
|  |  |_   _|     |  |     |     | __  |  _  | | | |  |  |   __| __  |
|     | | | | | | |  |__   |   --|    -|     | | | |  |__|   __|    -|
|__|__| |_| |_|_|_|_____|  |_____|__|__|__|__|_____|_____|_____|__|__|

'''

MENU = r'''
Choose a command:
[1] Create Tree Model
[2] Search by relative path
[3] Change Node
[4] Copy Node
[5] Save to file
[6] Visualize

[9] Еxit

'''


# Helper class for the different data types
class Tag(Enum):
    ENTRY_TAG = 1
    EXIT_TAG = 2
    NOT_TAG = 3


def get_file_extension(html_file_path):
    flag = False
    extension = ''

    # Getting the extension
    for char in html_file_path:
        if flag is True:
            extension += char
        if char == '.':
            flag = True

    return extension


def load_file(html_file_path):
    # Raise an error if extension is not "html"
    if get_file_extension(html_file_path) != 'html':
        raise Exception('The expected extension is "html"')

    # Try to open the specified file
    with open(html_file_path, 'r') as f:
        data = f.read()
        return data


def html_crawler_window():
    os.system('clear')
    print(HTML_CRAWLER)
    print(MENU)


def input_command():
    ALL_COMMANDS = ['1', '2', '3', '4', '5', '6', '9']

    command = input('Input: ')

    while command not in ALL_COMMANDS:
        html_crawler_window()
        print(f'Your last command was not recognized.\n')
        command = input('Input: ')
    return command


def get_html_element_type(tag):
    if len(tag) >= 3:
        if tag[:2] == '</' and tag[-1] == '>':
            return Tag.EXIT_TAG
        elif tag[0] == '<' and tag[-1] == '>':
            return Tag.ENTRY_TAG
        else:
            return Tag.NOT_TAG
    return Tag.NOT_TAG
