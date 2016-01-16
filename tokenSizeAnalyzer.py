__author__ = 'afaherty'

import os, re
from types import *


token_size = {}


#creates a dictionary object that counts how many times a word length is found in the file
def token_size_process_tokens(words) :

    global token_size

    for word in words :

        word = re.sub(r'[^\w\s]', '', word)

        token_size[len(word)] = token_size.get(len(word), 0) + 1


#writes generic token size analysis to output file
def write_token_data(file) :

    file.write("TOKEN SIZE ANALYSIS\n\n")

    count = 0

    #loop list to write words to file
    for word, value in token_size.items() :

        count += 1

        if count < len(token_size):

            file.write(str(word) + ':\t' + str(value) + '\n')

        else :

            file.write(str(word) + ':\t' + str(value))


#writes writes histogram of token size analysis to output file
def write_token_size_histogram(file):

    file.write('TOKEN SIZE HISTOGRAM\n\n')


#writes output to tokenSize.txt file
def token_size_output_file() :

    file_path = 'C:/Users/L/Dropbox/enterprisejava/pythonAnalyzer/output/tokenSize.txt'
    mode = 'a' if os.path.exists(file_path) else 'w+'

    with open(file_path, mode) as file :

        file.seek(0)
        file.truncate() #clears file if it exists already

        write_token_data(file)
        file.write('\n\n\n')
        write_token_size_histogram(file)