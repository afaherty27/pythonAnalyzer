__author__ = 'afaherty'

import os

# method compares words in keyword file to words in analysis file
def keyword_process_tokens(words) :

    with open('keywords.txt', 'r') as keyword_file :

        keywords = keyword_file.read().split()

        for keyword in keywords:

            index_list = []
            for index, word in enumerate(words) :

                if word.lower() == keyword :
                    index_list.append(index)

            write_keyword_data(keyword, index_list)


def write_keyword_data(keyword, index_list) :
    print(keyword + str(index_list))

def keyword_output_file(text_file) :
    print('hello keyword output')