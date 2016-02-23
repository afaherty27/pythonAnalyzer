__author__ = 'afaherty'

import os


# method compares words in keyword file to words in analysis file
def keyword_process_tokens(words) :


    file_path = 'C:/Users/L/Dropbox/enterprisejava/pythonAnalyzer/output/keywords.txt'
    mode = 'a' if os.path.exists(file_path) else 'w+'

    with open(file_path, mode) as file :

        file.seek(0)
        file.truncate() #clears file if it exists already

        with open('keywords.txt', 'r') as keyword_file :

            keywords = keyword_file.read().split()

            for keyword in keywords:

                index_list = []
                for index, word in enumerate(words) :

                    if word.lower() == keyword :
                        index_list.append(index)

                file.write(keyword + ' = ' + str(index_list) + '\n\n')