__author__ = 'afaherty'

import os, re

word_set = []

# removed duplicate instances of words in list
def unique_process_tokens(words) :

    global word_set

    edited_words = []

    for word in words :

        word = re.sub(r'[^\w\s]', '', word)
        edited_words.append(word)


    word_set = list(set(edited_words))


#writes output file of words list
def unique_token_output_file():

    file_path = 'C:/Users/L/Dropbox/enterprisejava/pythonAnalyzer/output/uniqueTokens.txt'
    mode = 'a' if os.path.exists(file_path) else 'w+'

    with open(file_path, mode) as file :

        file.seek(0)
        file.truncate() #clears file if it exists already

        word_set.sort()

        count = 0

        #loop list to write words to file
        for word in word_set :

            count += 1

            if count < len(word_set):

                file.write(word + '\n')

            else :

                file.write(word)