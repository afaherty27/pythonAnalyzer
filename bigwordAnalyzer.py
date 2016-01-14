__author__ = 'afaherty'

import os

minimum_word_length = 8
big_word_list = []


# processes list of words to include words that meet minimum length requirement
def bigword_process_tokens(words) :

    for word in words :

        if len(word) >= minimum_word_length :
            #print(word)
            big_word_list.append(word)


#prints output to bigwords.txt file
def bigword_output_file(text_file) :

    file_path = 'C:/Users/L/Dropbox/enterprisejava/pythonAnalyzer/output/bigwords.txt'
    mode = 'a' if os.path.exists(file_path) else 'w+'

    with open(file_path, mode) as file :

        file.seek(0)
        file.truncate() #clears file if it exists already

        big_word_list.sort()

        count = 0 #ref to count of index while looping list to remove blank space after final word in list

        #loop list to write words to file
        for word in big_word_list:

            count += 1

            if count < len(big_word_list) :

                file.write(word + '\n')

            else :

                file.write(word)