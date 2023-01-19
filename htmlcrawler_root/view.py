# External imports

# Internal imports
from htmlcrawler_root.utils import html_crawler_window, input_command
from htmlcrawler_root.crawler import Crawler


def welcome(file_data):
    # Create Crawler instance with data from file
    crawler = Crawler(file_data)

    # Different behaviours based on selected option
    menu_dict = {
        '1': crawler.create_tree,
        '2': crawler.search_relative_path,
        '3': crawler.change_node,
        '4': crawler.copy_node,
        '5': crawler.save_to_file,
        '6': crawler.visualize
    }

    # Show the main screen
    html_crawler_window()

    # Get the command
    command = input_command()

    # Execute the selected command and refresh or exit
    while command != '9':
        menu_dict[command]()
        html_crawler_window()
        command = input_command()
