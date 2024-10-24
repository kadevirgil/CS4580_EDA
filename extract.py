"""File for extracting data from the database and saving it to a csv file"""

import os
from zipfile import ZipFile, is_zipfile


# Constants
FILE_NAME = "english-premier-league.zip"


def extract_data(file_path: str):
    """Extracts data from the zip file into the data directory

    Args:
        file_path (str): The path to the zip file
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print("The file does not exist")
        return

    # Check if the file is a zip file
    if is_zipfile(file_path):
        with ZipFile(file_path, "r") as file:
            file.extractall(os.path.join(os.getcwd(), "data"))

        # Remove the zip file after extracting the data
        os.remove(file_path)

    else:
        print("The file is not a zip file")
        return


def main():
    """Driver function for the file"""
    extract_data(FILE_NAME)


if __name__ == "__main__":
    main()
