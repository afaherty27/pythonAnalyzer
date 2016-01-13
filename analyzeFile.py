__author__ = 'afaherty'
from summaryReport import summary_process_tokens
from summaryReport import summary_write_output_file
from uniqueTokenAnalyzer import unique_process_tokens
from uniqueTokenAnalyzer import unique_token_output_file


def process_tokens(words) :
    summary_process_tokens(words)
    unique_process_tokens(words)


def write_output_files(text_file) :
    summary_write_output_file(text_file)
    unique_token_output_file(text_file)

# input to hold file
print('enter file to read:')
file_name = input()

# open file to read
with open(file_name, 'r') as text_file :

    words = text_file.read().split()
    #works for small file. not large
    process_tokens(words)
    write_output_files(text_file)

    
