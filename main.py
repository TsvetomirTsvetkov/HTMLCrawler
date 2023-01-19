# External imports
import argparse

# Internal imports
from htmlcrawler_root.view import welcome
from htmlcrawler_root.utils import load_file


def parser():
    # Create an ArgumentParser instance and expect an HTML file to be passed
    parser = argparse.ArgumentParser(description='HTML Crawler')
    parser.add_argument('html_file_path', metavar='<html_file_path>', type=str, help='The path to the HTML file')

    # Check whether the input is as expected
    args = parser.parse_args()

    return args


def main():
    args = parser()

    # Try to load the HTML file
    file_data = load_file(args.html_file_path)

    # Start the application
    welcome(file_data)


if __name__ == '__main__':
    main()
