__author__ = 'afaherty'

import os

# This module parses the word list, and finds the unique words in the list
unique_words = []

def unique_process_tokens(words) :

    global unique_words
    unique_words = list(set(words))


def unique_token_output_file():
    # TODO complete variables to complete report

    file_path = 'C:/Users/Adam/Dropbox/enterprisejava/pythonAnalyzer/uniqueTokens.txt'
    mode = 'a' if os.path.exists(file_path) else 'w+'

    with open(file_path, mode) as file :

        file.seek(0)
        file.truncate() #clears file if it exists already
        # TODO complete file.write() for report