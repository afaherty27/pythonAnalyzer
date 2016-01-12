__author__ = 'afaherty'
from summaryReport import summary_process_tokens
from summaryReport import summary_write_output_file


def process_tokens(text_file) :
    summary_process_tokens(words)


def write_output_files(text_file) :
    summary_write_output_file(text_file)


# input to hold file
print('enter file to read:')
file_name = input()

# open file to read
with open(file_name, 'r') as text_file :

    words = text_file.read().split()
    #summary_process_tokens(words)

    process_tokens(text_file)
    write_output_files(text_file)