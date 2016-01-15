__author__ = 'afaherty'

import os, re

# this module counts how many times each word appears in the list

token_counts = {}
longest_string = 0

#creates a dictionary object that counts how many times each word is in the file
def token_count_process_tokens(words) :

    global token_counts

    for word in words :

        word = re.sub(r'[^\w\s]', '', word)
        token_counts[word] = token_counts.get(word, 0) + 1

    find_longest_string_length(words)


#determines what longest string length is for output file formating
def find_longest_string_length(words) :

    global longest_string
    longest_string = max(len(word) for word in words)
    print(longest_string)


# writes results to tokenCount.txt
def token_count_output_file() :

    file_path = 'C:/Users/L/Dropbox/enterprisejava/pythonAnalyzer/output/tokenCount.txt'
    mode = 'a' if os.path.exists(file_path) else 'w+'

    with open(file_path, mode) as file :

        file.seek(0)
        file.truncate() #clears file if it exists already

        count = 0

        #loop list to write words to file
        for word, value in token_counts.items() :

            count += 1

            if count < len(token_counts):

                file.write(word + ':'.ljust(longest_string - len(word)) + '\t' + str(value) + '\n')

            else :

                file.write(word + ':'.ljust(longest_string - len(word)) + '\t' + str(value))
